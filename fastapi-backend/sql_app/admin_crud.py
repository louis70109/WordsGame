from sqlalchemy.orm import Session

from . import models, schemas


def get_games(db: Session, skip: int = 0, limit: int = 12):
    return db.query(models.Game).offset(skip).limit(limit).order_by("score desc, level desc").all()


def get_styles(db: Session):
    return db.query(models.Style).all()


def set_styles(db: Session, style: schemas.StyleCreate):
    styles = get_styles(db=db)
    for idx in range(len(styles)):
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
