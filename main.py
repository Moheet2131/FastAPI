


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 2️. User Model (Data Structure)

class UserInfo(BaseModel):
    name: str
    email: str
    age: int


# For PATCH (partial update):

class UpdateUserInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None



# 3️. Temporary Database (In-Memory)

user_db = {}


# 4️. POST – Create User

@app.post("/user_info/{user_id}")
def create_user(user_id: int, user: UserInfo):
    user_db[user_id] = user
    return {
        "message": "User created successfully",
        "data": user
    }


# 5️. GET – Fetch User

@app.get("/user_info/{user_id}")
def get_user(user_id: int):
    return user_db.get(user_id, "User not found")



# 6️. PUT – Full Update User


@app.put("/user_info/{user_id}")
def update_user(user_id: int, user: UserInfo):
    user_db[user_id] = user
    return {
        "message": "User fully updated",
        "data": user
    }



# 8️. DELETE – Remove User


@app.delete("/user_info/{user_id}")
def delete_user(user_id: int):
    user_db.pop(user_id, None)
    return {"message": "User deleted successfully"}



