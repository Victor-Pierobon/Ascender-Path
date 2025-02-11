from pydantic import BaseModel
from enum import Enum


class QuestType(str, Enum):
    NORMAL = "normal"
    DAILY = "daily"


class QuestBase(BaseModel):
    title: str
    description: str
    type: QuestType
    stat_name: str
    xp_reward: int


class QuestCreate(QuestBase):
    pass

class Quest(QuestBase):
    id: int


    class Config:
        orm_mode = True