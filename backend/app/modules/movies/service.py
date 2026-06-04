from sqlalchemy.orm import Session

from app.modules.movies.models import Movie
from app.modules.movies.repository import (
    MovieRepository,
)
from app.modules.movies.schemas import (
    MovieCreate,
    MovieUpdate,
)


class MovieService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = MovieRepository(db)

    def get_all_movies(self):
        return self.repository.get_all()

    def get_movie(
        self,
        movie_id: int,
    ):
        movie = self.repository.get_by_id(
            movie_id
        )

        if not movie:
            raise ValueError(
                "Movie not found"
            )

        return movie

    def create_movie(
        self,
        payload: MovieCreate,
    ):
        movie = Movie(
            title=payload.title,
            description=payload.description,
            duration_minutes=payload.duration_minutes,
            genre=payload.genre,
            language=payload.language,
            poster_url=payload.poster_url,
            is_active=payload.is_active,
        )

        return self.repository.create(
            movie
        )

    def update_movie(
        self,
        movie_id: int,
        payload: MovieUpdate,
    ):
        movie = self.repository.get_by_id(
            movie_id
        )

        if not movie:
            raise ValueError(
                "Movie not found"
            )

        update_data = (
            payload.model_dump(
                exclude_unset=True
            )
        )

        for key, value in update_data.items():
            setattr(
                movie,
                key,
                value,
            )

        return self.repository.update(
            movie
        )

    def delete_movie(
        self,
        movie_id: int,
    ):
        movie = self.repository.get_by_id(
            movie_id
        )

        if not movie:
            raise ValueError(
                "Movie not found"
            )

        self.repository.delete(movie)