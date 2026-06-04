from pydantic import BaseModel
from pydantic import ConfigDict

from datetime import datetime


class MovieBase(BaseModel):
    title: str
    description: str | None = None
    duration_minutes: int
    genre: str
    language: str
    poster_url: str | None = None
    is_active: bool = True


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    duration_minutes: int | None = None
    genre: str | None = None
    language: str | None = None
    poster_url: str | None = None
    is_active: bool | None = None


class MovieResponse(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )