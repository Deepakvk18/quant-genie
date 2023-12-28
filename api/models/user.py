from pydantic import BaseModel, Field
from bson import ObjectId

class UserModel(BaseModel):
    id: str = Field(alias='_id')
    email: str
    img: str = None
    openai_api_key: str = None
    google_api_key: str = None
    fmp_api_key: str = None
    news_api_key: str = None