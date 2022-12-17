from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}


@app.post("/createposts")
def create_post():
    return {"message":"successfully created posts"}


