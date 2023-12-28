from pydantic import BaseModel

class SuccessMessage(BaseModel):
    message: str