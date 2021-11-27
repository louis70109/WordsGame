from sqlalchemy.orm import Session

from . import models, schemas


def db_commit(db: Session, db_model):
    db.add(db_model)
    db.commit()
    db.refresh(db_model)


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(uid=user.uid, name=user.name, picture=user.picture)
    db_commit(db, db_user)
    return db_user


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).order_by("score desc, level desc").all()


def create_user_game(db: Session, game: schemas.GameCreate, user_id: str):
    game.owner_id = user_id
    db_game = models.Game(**game.dict())
    try:
        db_commit(db, db_game)
    except Exception as e:
        raise Exception('Game commit error', e)
    return db_game

def get_games(db: Session, limit: int = 20):
    return db.query(models.Game).order_by(
        models.Game.level.desc(), models.Game.score.desc()).limit(limit).all()


def get_user_games(db: Session, user_id: str, skip: int = 0, limit: int = 20):
    return db.query(models.Game).filter(
        models.Game.owner_id == user_id).offset(skip).limit(limit).all()


def get_user_game(db: Session, user_id: str, level: int = 1):
    return db.query(models.Game).filter(
        models.Game.owner_id == user_id,
        models.Game.level == level
    ).first()


def get_user_style(db: Session, user_id: str):
    return db.query(models.Style).filter(
        models.Style.owner_id == user_id).first()


def create_user_style(db: Session, style: schemas.StyleCreate, user_id: str):
    style.owner_id = user_id
    db_style = models.Style(**style.dict())
    try:
        db_commit(db, db_style)
    except Exception as e:
        raise Exception("create style error")
    return db_style
