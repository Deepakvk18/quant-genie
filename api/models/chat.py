from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId

class Message(BaseModel):
    input: str
    output: str

class ChatModel(BaseModel):
    id: str = Field(alias='_id')
    user_id: str
    title: str
    messages: List[Message]