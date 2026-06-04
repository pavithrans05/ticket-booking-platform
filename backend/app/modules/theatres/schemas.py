from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TheatreBase(BaseModel):
    name: str
    city: str
    address: str
    total_screens: int
    is_active: bool = True

class TheatreCreate(TheatreBase):
    pass

class TheatreUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    address: str | None = None
    total_screens: int | None = None
    is_active: bool | None = None

class TheatreResponse(TheatreBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)