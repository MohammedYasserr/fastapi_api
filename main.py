from fastapi import FastAPI 
from fastapi.params import Body

app = FastAPI() 


@app.get("/")
async def root():
    return {'message' : 'Hello, Bemo'}


@app.get("/posts")
async def get_posts():
    return {'posts' : 'This to test postman and the url is working'}


@app.post("/createPosts")
async  def create_posts(payload : dict = Body(...)):
    print(payload)
    return {"message" : f"title: {payload['title']} content: {payload['content']}"}

