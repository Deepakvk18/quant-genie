from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Output(BaseModel):
    text: str
    images: List[str]

class Message(BaseModel):
    input: str
    output: Output

class ChatModel(BaseModel):
    id: str| None = Field(alias='_id')
    user_id: str
    title: str
    messages: List[Message]
    chat_history: str | None
    last_accessed_date: datetime | None