from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

import db
from models import User, UserUpdateRequest

app = FastAPI()

@app.get("/")
async def hello_world ():
    return {"message": "Hello World"}

@app.get("/api/v1/users", response_model=List[User])
async def fetch_users ():
    return db.dbList

@app.post("/api/v1/users", status_code=201)
async def register_user(user: User):
    db.dbList.append(user)
    return {"User": user}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db.dbList:
        if user.id == user_id:
            db.dbList.remove(user)
            return {
                    "Deleted": True,
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                    }
    raise   HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    ) 
    
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db.dbList:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {
                "Updated": True,
                "User": user
            }
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )        