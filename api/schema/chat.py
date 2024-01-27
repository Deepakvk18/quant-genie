from pydantic import BaseModel
from typing import List
from models.chat import Message, ChatModel

class CreateChat(BaseModel):
    user_id: str
    messages: List[Message]
    title: str

class CreateChatSuccess(BaseModel):
    message: str
    chat_id: str

class UpdateChat(BaseModel):
    chat_id: str
    messages: List[Message]

class Chats(BaseModel):
    chats: List[ChatModel]