from pydantic import BaseModel
from typing import List
from data_models.stat import Stat

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    level: int 
    stats: List[Stat] = []

    class Config:
        orm_mode = True