from fastapi import FastAPI 


app = FastAPI() 


@app.get("/")
async def root():
    return {'message' : 'Hello, Bemo'}


@app.get("/posts")
async def get_posts():
    return "This is my posts lists"