import os
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request, Depends
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage
from pydantic import BaseModel
from sql_app.admin_crud import set_styles
from sql_app import schemas
from sql_app.database import get_db

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET', None))


router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None), ):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    text = event.message.text
    response = "hi"
    if text == 'a':
        response = set_styles(db=next(get_db()), style=schemas.StyleCreate(
            color='#000000',
            size='50px',
            duration=20,
            level=0,
        ))
    elif text == 's':
        response = set_styles(db=next(get_db()), style=schemas.StyleCreate(
            color='#000000',
            size='30px',
            duration=10,
            level=1,
        ))
    elif text == 'd':
        response = set_styles(db=next(get_db()), style=schemas.StyleCreate(
            color='#000000',
            size='18px',
            duration=7,
            level=3,
        ))
    reply_event = TextSendMessage(text=str(response))
    line_bot_api.reply_message(
        event.reply_token,
        reply_event
    )
