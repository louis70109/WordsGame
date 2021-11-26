from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app import schemas, crud
from sql_app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "User Not found"}},
)


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_specific_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    return user


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.uid)
    if db_user:
        print("User already registered")
        return db_user
    return crud.create_user(db=db, user=user)


@router.post("/{user_id}/games/", response_model=schemas.Game)
def create_user_games(user_id: str, game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    game = crud.create_user_game(db, game=game, user_id=user_id)
    return game


@router.get("/{user_id}/games/", response_model=List[schemas.Game])
def read_user_games(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    user_games = crud.get_user_games(db, user_id=user_id, limit=10)
    return user_games


@router.get("/{user_id}/games/{level}", response_model=List[schemas.Game])
def read_user_games_level(user_id: str, level: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    user_games = crud.get_user_game(db, user_id=user_id, level=int(level))
    return user_games


@router.get("/{user_id}/style/", response_model=schemas.Style)
def read_user_style(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    user_style = crud.get_user_style(db, user_id=user_id)
    return user_style


@router.post("/{user_id}/style/", response_model=schemas.Style)
def create_user_style(user_id: str, style: schemas.StyleCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    style = crud.create_user_style(db, style=style, user_id=user_id)
    return style
