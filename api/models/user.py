from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    email: str
    img: str = None
    openai_api_key: str = None
    google_api_key: str = None
    fmp_api_key: str = None
    news_api_key: str = None