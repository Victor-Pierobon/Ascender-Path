from fastapi import FastAPI
from data_models.stat import Stat, StatCreate, StatBase
from data_models.user import User, UserCreate, UserBase
from data_models.quest import Quest, QuestCreate, QuestBase


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Ascender Path API"}

@app.get("/quests/")
async def read_quests():
    #
    return [{"id": 1, "title": "learn FastAPI Basics", "completed": False}]

@app.get("/users/{user_id}/stats/")
async def get_user_stats(user_id, int):
    pass