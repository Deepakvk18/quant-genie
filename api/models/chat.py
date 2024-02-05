from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Output(BaseModel):
    text: str
    images: List[str]

class Message(BaseModel):
    id: str| None = Field(alias='_id')
    chat_id: str
    input: str
    output: Output
    time_of_message: datetime | None

class ChatModel(BaseModel):
    id: str| None = Field(alias='_id')
    user_id: str
    title: str
    chat_history: str | None = None
    last_accessed_date: datetime | None