from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# we are going to validate the data that we are receiving here
class Post(BaseModel):
    title: str  
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post(post: Post): # we are going to validate the data based on the pydantic model
    print(post)
    print(post.dict())
    return {"data": post}

