from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app import schemas, crud
from sql_app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
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
    db_user = crud.get_user_by_uid(db, user_id=user.uid)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@router.post("/{user_id}/projects/", response_model=schemas.Project)
def create_user_projects(user_id: str, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_uid(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    project = crud.create_user_project(db, project=project, user_id=user_id)
    return project


@router.get("/{user_id}/projects/", response_model=List[schemas.Project])
def read_user_projects(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_uid(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not registered")
    user_projects = crud.get_user_projects(db, user_id=user_id)
    return user_projects
