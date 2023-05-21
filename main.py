from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI() 


# constructing a class that defines the schema structure

class Post(BaseModel):
    title: str 
    content : str
    published : bool = True
    rating : Optional[int] = None


# Setting up a hard-coded variable to store our posts 

my_posts = [
            {"title" :"This is the title of post 1", "content" :"this is content of post 1" , "id" : 1}, 
            {"title":"fav foods", "content" : "Fired fish is my fav food", "id": 2}
] 

@app.get("/")
def root():
    return {'message' : 'Hello, Bemo'} 


@app.get("/posts")
def get_posts():
    return {"data" : my_posts}


@app.post("/createposts")
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post)
    return {"Data" : post_dict}

