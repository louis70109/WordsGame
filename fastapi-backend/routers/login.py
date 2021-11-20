import logging
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import requests
import json
from sql_app import schemas, crud
from sql_app.database import get_db
from pydantic import BaseModel
from utils.verify import decode_id_token

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "LINE Login not found"}},
)


@router.post("/")
def read_users(code: str, state: str, db: Session = Depends(get_db)):
    client_id = os.environ.get('LINE_LOGIN_CLIENT_ID')
    secret = os.environ.get('LINE_LOGIN_SECRET')
    r = requests.post(
        "https://api.line.me/oauth2/v2.1/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": os.environ.get('LINE_LOGIN_URI'),
            "client_id": client_id,
            "client_secret": secret,
        }, headers={"Content-Type": "application/x-www-form-urlencoded"})
    payload = json.loads(r.text)
    token = payload.get("id_token")
    if token is None:
        logger.info('Token payload is empty' + payload)
        return {'result': payload['error_description']}, 400

    try:
        verify_result = decode_id_token(token, client_id, secret)
        logger.info('LINE login result: ' + str(verify_result))
    except Exception as e:
        logger.warn('Login warring....' + str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {
        'uid': verify_result.get('sub'),
        'name': verify_result.get('name'),
        'picture': verify_result.get('picture')
    }


@router.get("/uri")
def get_line_login_link():
    r_uri = os.environ.get("LINE_LOGIN_URI")
    client = os.environ.get("LINE_LOGIN_CLIENT_ID")
    state = "nostate" # it will be random value
    uri = f"https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id={client}&redirect_uri={r_uri}&scope=profile%20openid%20email&state={state}&initial_amr_display=lineqr"
    logger.info('Login url is: ' + uri)
    return {'result': uri}
