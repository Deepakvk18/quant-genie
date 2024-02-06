from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional, Annotated
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]

class Output(BaseModel):
    text: str
    images: List[str] = []

class Message(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    chat_id: str
    input: str
    output: Output
    time_of_message: datetime | None

class ChatModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    user_id: str
    title: str = 'New Chat'
    chat_history: str = ''
    last_accessed_date: datetime | None