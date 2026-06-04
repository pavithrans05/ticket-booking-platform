from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    model_config = {
        "from_attributes": True
    }