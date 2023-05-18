from fastapi import FastAPI 
from fastapi.params import Body

app = FastAPI() 


@app.get("/")
def root():
    return {'message' : 'Hello, Bemo'} # Whatever we are returing here is what will be sent to the user 


@app.get("/posts")
def get_posts():
    return {'posts' : 'This to test postman and the url is working'} # This is what client recives when the endpoint got hit ... 


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {'New Post': f"title: {payload['title']} content: {payload['content']}"}

