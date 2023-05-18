from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI() 


# constructing a class that defines the schema structure

class Post(BaseModel):
    title: str 
    content : str
    published : bool = True
    rating : Optional[int] = None


@app.get("/")
def root():
    return {'message' : 'Hello, Bemo'} # Whatever we are returing here is what will be sent to the user 


@app.get("/posts")
def get_posts():
    return {'posts' : 'This to test postman and the url is working'} # This is what client recives when the endpoint got hit ... 


@app.post("/createposts")
def create_posts(new_post : Post):
    print(new_post.rating)
    return {"Data" : "New Post"}

