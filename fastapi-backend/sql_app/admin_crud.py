from sqlalchemy.orm import Session

from . import models, schemas


def db_commit(db: Session, db_model):
    db.add(db_model)
    db.commit()
    db.refresh(db_model)


def get_games(db: Session, skip: int = 0, limit: int = 12):
    return db.query(models.Game).offset(skip).limit(limit).order_by("score desc, level desc").all()


def set_games(db: Session):
    return db.query(models.Game).order_by("score desc, level desc").all()


def get_user_game(db: Session, user_id: str, level: int = 1):
    return db.query(models.Game).filter(
        models.Game.owner_id == user_id,
        models.Game.level == level
    ).first()


def get_styles(db: Session):
    return db.query(models.Style).all()


def set_styles(db: Session, style: schemas.StyleCreate):
    styles = get_styles(db=db)
    for idx in range(len(styles)):
        print(styles[idx].owner_id)
        print(style.dict())
        styles[idx].size = style.size
        styles[idx].color = style.color
        styles[idx].duration = style.duration
        styles[idx].level = style.level
        
        db.query(models.Style).filter(models.Style.id == styles[idx].id)
        db.add(styles[idx])
    try:
        db.commit()
        db.close()
    except Exception:
        raise Exception("create style error")
    return style
