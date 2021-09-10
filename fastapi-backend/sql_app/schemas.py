from typing import List, Optional

from pydantic import BaseModel


class GameBase(BaseModel):
    score: str
    level: str
    owner_id: Optional[str]


class GameCreate(GameBase):
    pass


class Game(GameBase):
    class Config:
        orm_mode = True


class StyleBase(BaseModel):
    score: str
    level: str
    owner_id: Optional[str]


class StyleCreate(StyleBase):
    pass


class Style(StyleBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    uid: str
    name: str
    picture: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    Games: List[Game] = []

    class Config:
        orm_mode = True
