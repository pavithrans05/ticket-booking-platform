from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class ShowBase(BaseModel):
    movie_id: int
    start_time: datetime
    end_time: datetime
    price: float
    is_active: bool = True


class ShowCreate(ShowBase):
    pass


class ShowUpdate(BaseModel):
    movie_id: int | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    price: float | None = None
    is_active: bool | None = None


class ShowResponse(ShowBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )