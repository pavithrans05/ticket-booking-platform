from sqlalchemy.orm import Session

from app.modules.movies.models import Movie


class MovieRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_all(self):
        return (
            self.db.query(Movie)
            .order_by(Movie.id.desc())
            .all()
        )

    def get_by_id(
        self,
        movie_id: int,
    ):
        return (
            self.db.query(Movie)
            .filter(Movie.id == movie_id)
            .first()
        )

    def create(
        self,
        movie: Movie,
    ):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)

        return movie

    def update(
        self,
        movie: Movie,
    ):
        self.db.commit()
        self.db.refresh(movie)

        return movie

    def delete(
        self,
        movie: Movie,
    ):
        self.db.delete(movie)
        self.db.commit()