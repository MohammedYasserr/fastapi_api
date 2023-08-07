from fastapi import FastAPI, Response , status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

# Creating an instance of FASTAPI 
app = FastAPI() 



# constructing a class that defines the schema structure
class Post(BaseModel):
    title: str 
    content : str
    published : bool = True
    rating : Optional[int] = None


# Setting up a hard-coded variable to store our posts - Fake DB 
my_posts = [{"title" :"This is the title of post 1", "content" :"this is content of post 1" , "id" : 1},{"title":"fav foods", "content" : "Fired fish is my fav food", "id": 2}] 

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# Get enpoint..... 
@app.get("/")
def root():
    return {'message' : 'Hello, world'} 


@app.get("/posts")
def get_posts():
    return {"data" : my_posts}



@app.post("/createposts" , status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post)
    return {"Data" : post_dict}


# getting and retring the lastes post

@app.get('/posts/latest')
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"details": post}



# Getting a post given a specific id - This {id} is going to be send dynamically by the user.
# {id} is called a path parameter
@app.get('/posts/{id}')
def get_posts(id:int, response: Response):
    post =find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"post with id {id}: was not found")
    return {"post detail" : post}


