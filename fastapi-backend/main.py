import os
from sqlalchemy.engine import create_engine

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn
import sql_app.database as db
import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from routers import users, login

logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup() -> None:
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URI')
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    db.Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown():
    db.SessionLocal().close()
    

# app.include_router(webhooks.router)
app.include_router(users.router)
app.include_router(login.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/web", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0"
                , port=5000, reload=True
                )
