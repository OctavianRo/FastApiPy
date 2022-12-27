from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
# from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session 

# need to debug
from . import models  
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# we are going to validate the data that we are receiving here
class Post(BaseModel):
    title: str  
    content: str
    published: bool = True

# keep trying to connect ot the database 
while True:
    try:
        conn = psycopg2.connect(
            host="localhost", 
            database="fastapi", 
            user="postgres", 
            password="Trumpet79?", 
            cursor_factory=RealDictCursor
        )

        cursor = conn.cursor()
        print("Database connection was successful!")
        break


    except Exception as error:
        print("Connecting to database failed :(")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "successfully connected"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data":posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post): # we are going to validate the data based on the pydantic model

    # sanitizing inputs with the %s method 
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    # we have to commit these changes to db
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int): # this is a path parameter
    # no SQL injections
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

# returning 404 on error
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id), ))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist") 

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post): # we are going to convert it to an int
    cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post=cursor.fetchone()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    return {"data": updated_post}

