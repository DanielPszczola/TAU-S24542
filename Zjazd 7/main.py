from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock database
users_db = {}
current_id = 1


class User(BaseModel):
    name: str
    email: str


@app.get("/users")
def get_users():
    return list(users_db.values())


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@app.post("/users", status_code=201)
def create_user(user: User):
    global current_id
    user_data = {"id": current_id, **user.model_dump()}
    users_db[current_id] = user_data  # Save the user
    current_id += 1
    return user_data


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].update(user.model_dump())
    return users_db[user_id]


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}
