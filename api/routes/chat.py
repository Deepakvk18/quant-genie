from fastapi import APIRouter, Depends, Security
from database.messages import ChatRepo, MessageRepo
from schema.chat import Chats, GetMessages
from models.chat import ChatModel
from utils import get_settings
from fastapi_jwt import JwtAuthorizationCredentials
from utils import get_settings

from .extensions import access_security

settings = get_settings()

chat_router = APIRouter(tags=["chats"])

@chat_router.get('/chat/{chat_id}', response_model=ChatModel)
async def get_chat(chat_id:str, credentials: JwtAuthorizationCredentials = Security(access_security), chats: ChatRepo = Depends()):
    chat = chats.get_chat(chat_id)
    chat['_id'] = str(chat['_id'])
    return chat

@chat_router.get('/chats', response_model=Chats)
async def get_chats(credentials: JwtAuthorizationCredentials = Security(access_security), chat: ChatRepo = Depends()):
    user_id = credentials.subject.get('userId')
    chats = chat.get_chats(user_id)
    return { 'chats': chats }

@chat_router.get('/messages/{chat_id}', response_model=GetMessages)
async def get_messages(chat_id: str, credentials: JwtAuthorizationCredentials = Security(access_security), messages: MessageRepo = Depends()):
    messages = messages.get_messages(chat_id=chat_id)
    return {'messages': messages}
