from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

import db
from models import User

app = FastAPI()

@app.get("/")
async def hello_world ():
    return {"message": "Hello World"}

@app.get("/api/v1/users", response_model=List[User])
async def fetch_users ():
    return db.db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id: UUID):
    for user in db.db:
        if user.id == user_id:
            db.db.remove(user)
            return
        