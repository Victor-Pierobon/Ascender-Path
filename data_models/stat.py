from pydantic import BaseModel

class StatBase(BaseModel):
    name: str
    level: int = 0
    xp: int = 0
    xp_to_level_up = int =  5 + level * (1.25 + level/10)

class StatCreate(StatBase):
    pass

class Stat(StatBase):
    id: int

    class Config:
        orm_mode = True