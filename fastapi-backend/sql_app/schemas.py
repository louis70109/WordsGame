from typing import List, Optional

from pydantic import BaseModel


class GameBase(BaseModel):
    score: str
    level: str
    owner_id: Optional[str]


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    class Config:
        orm_mode = True


class StyleBase(BaseModel):
    size: str
    color: str
    duration: int
    level: int
    owner_id: Optional[str]


class StyleCreate(StyleBase):
    pass


class Style(StyleBase):
    id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    uid: str
    name: str
    picture: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    games: List[Game] = []
    styles: List[Style] = []

    class Config:
        orm_mode = True
