from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from sql_app import schemas, crud
from sql_app.database import get_db

router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={404: {"description": "Games Not found"}},
)


@router.get("/", response_model=List[schemas.Game])
def read_user_games(db: Session = Depends(get_db)):
    user_games = crud.get_games(db, limit=10)
    return user_games
