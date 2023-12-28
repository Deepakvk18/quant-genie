from pydantic import BaseModel, Field
from typing import Optional
from models.user import UserModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserCreateResponse(BaseModel):
    message: str
    user_id: str

class UserPatch(BaseModel):
    img: Optional[str] = None
    fmp_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    news_api_key: Optional[str] = None

class LoginResponse(BaseModel):
    access_token: str
    user: UserModel