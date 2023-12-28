from fastapi import FastAPI
from routes.chat import chat_router
from routes.user import user_router
from utils import get_settings


app = FastAPI()

settings = get_settings()

app.include_router(chat_router)
app.include_router(user_router)

