from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated, List, Optional

# Create a FastAPI Application
app=FastAPI()

# this is home or local page http://127.0.0.1:8000/
@app.get("/")
async def Home():
    return {"This is my First Home Page using Fast API"}

# to open this page your url is http://127.0.0.1:8000/users/me/
@app.get("/users/me")
async def who_am_i():
    return {"user_id":"the current user"}

# to get data in query form url is http://127.0.0.1:8000/users/2
# you will get 2 in your output
@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return{"user_id":user_id}




