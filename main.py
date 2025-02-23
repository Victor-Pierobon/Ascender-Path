from fastapi import FastAPI, HTTPException
from data_models.user import User, UserCreate
from database import create_user_and_stats


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Ascender Path API"}

@app.post("/users/", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """Resgister a new User"""
    user_id = create_user_and_stats(user.username)
    if user_id:
        create_user = User(id=user_id, username=user.username, level=1, stats=[])
        return create_user
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")