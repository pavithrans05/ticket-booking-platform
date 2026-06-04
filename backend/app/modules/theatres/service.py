from sqlalchemy.orm import Session

from app.modules.theatres.models import Theatre
from app.modules.theatres.repository import TheatreRepository
from app.modules.theatres.schemas import (
    TheatreCreate,
    TheatreUpdate,
)


class TheatreService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = TheatreRepository(db)

    def get_all_theatres(self):
        return self.repository.get_all()

    def get_theatre(
        self,
        theatre_id: int,
    ):
        theatre = self.repository.get_by_id(
            theatre_id
        )

        if not theatre:
            raise ValueError(
                "Theatre not found"
            )

        return theatre

    def create_theatre(
        self,
        payload: TheatreCreate,
    ):
        theatre = Theatre(
            name=payload.name,
            city=payload.city,
            address=payload.address,
            total_screens=payload.total_screens,
            is_active=payload.is_active,
        )

        return self.repository.create(
            theatre
        )

    def update_theatre(
        self,
        theatre_id: int,
        payload: TheatreUpdate,
    ):
        theatre = self.repository.get_by_id(
            theatre_id
        )

        if not theatre:
            raise ValueError(
                "Theatre not found"
            )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                theatre,
                key,
                value,
            )

        return self.repository.update(
            theatre
        )

    def delete_theatre(
        self,
        theatre_id: int,
    ):
        theatre = self.repository.get_by_id(
            theatre_id
        )

        if not theatre:
            raise ValueError(
                "Theatre not found"
            )

        self.repository.delete(
            theatre
        )