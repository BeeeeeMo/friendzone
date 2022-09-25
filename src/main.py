from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/login")
# async def login(user: User):
#     return {"message": "Hello World"}


@app.post("/register/")
async def register():
    pass
