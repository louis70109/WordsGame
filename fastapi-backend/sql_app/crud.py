from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_user_by_uid(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(uid=user.uid, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_user_game(db: Session, game: schemas.GameCreate, user_id: str):
    game.owner_id = user_id
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_user_games(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(
        models.Game.owner_id == user_id).offset(skip).limit(limit).all()
