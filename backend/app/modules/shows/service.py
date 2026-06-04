from sqlalchemy.orm import Session

from app.modules.movies.repository import (
    MovieRepository,
)

from app.modules.shows.models import Show

from app.modules.shows.repository import (
    ShowRepository,
)

from app.modules.shows.schemas import (
    ShowCreate,
    ShowUpdate,
)


class ShowService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = ShowRepository(db)
        self.movie_repository = MovieRepository(db)

    def get_all_shows(self):
        return self.repository.get_all()

    def get_show(
        self,
        show_id: int,
    ):
        show = self.repository.get_by_id(
            show_id
        )

        if not show:
            raise ValueError(
                "Show not found"
            )

        return show

    def create_show(
        self,
        payload: ShowCreate,
    ):
        movie = (
            self.movie_repository.get_by_id(
                payload.movie_id
            )
        )

        if not movie:
            raise ValueError(
                "Movie not found"
            )

        if (
            payload.end_time
            <=
            payload.start_time
        ):
            raise ValueError(
                "End time must be after start time"
            )

        show = Show(
            movie_id=payload.movie_id,
            start_time=payload.start_time,
            end_time=payload.end_time,
            price=payload.price,
            is_active=payload.is_active,
        )

        return self.repository.create(
            show
        )

    def update_show(
        self,
        show_id: int,
        payload: ShowUpdate,
    ):
        show = self.repository.get_by_id(
            show_id
        )

        if not show:
            raise ValueError(
                "Show not found"
            )

        update_data = (
            payload.model_dump(
                exclude_unset=True
            )
        )

        if "movie_id" in update_data:

            movie = (
                self.movie_repository.get_by_id(
                    update_data["movie_id"]
                )
            )

            if not movie:
                raise ValueError(
                    "Movie not found"
                )

        for key, value in update_data.items():
            setattr(
                show,
                key,
                value,
            )

        if (
            show.end_time
            <=
            show.start_time
        ):
            raise ValueError(
                "End time must be after start time"
            )

        return self.repository.update(
            show
        )

    def delete_show(
        self,
        show_id: int,
    ):
        show = self.repository.get_by_id(
            show_id
        )

        if not show:
            raise ValueError(
                "Show not found"
            )

        self.repository.delete(show)