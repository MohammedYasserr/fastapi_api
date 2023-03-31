from fastapi import FastAPI 


app = FastAPI() 


@app.get("/")
async def root():
    return {'message' : 'Hello, Bemo'}


@app.get("/posts")
async def get_posts():
    return {'posts' : 'This to test postman and the url is working'}


@app.post("/createPosts")
async  def create_posts():
    return {'msg' : 'Post was Created ! '}