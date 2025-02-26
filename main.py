from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated, List, Optional


# Create a FastAPI Application
app=FastAPI()




@app.get("/")
async def Home():
    return {"This is my First Home Page using Fast API"}


@app.get("/users/me")
async def who_am_i():
    return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return{"user_id":user_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items={"q":q}
    return query_items

