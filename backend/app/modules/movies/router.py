from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.modules.movies.schemas import (
    MovieCreate,
    MovieUpdate,
    MovieResponse,
)

from app.modules.movies.service import (
    MovieService,
)

from app.modules.auth.dependencies import (
    require_admin,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "",
    response_model=list[MovieResponse],
)
def get_movies(
    db: Session = Depends(get_db),
):
    return (
        MovieService(db)
        .get_all_movies()
    )


@router.get(
    "/{movie_id}",
    response_model=MovieResponse,
)
def get_movie(
    movie_id: int,
    db: Session = Depends(get_db),
):
    try:
        return (
            MovieService(db)
            .get_movie(movie_id)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "",
    response_model=MovieResponse,
)
def create_movie(
    payload: MovieCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    return (
        MovieService(db)
        .create_movie(payload)
    )


@router.put(
    "/{movie_id}",
    response_model=MovieResponse,
)
def update_movie(
    movie_id: int,
    payload: MovieUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:
        return (
            MovieService(db)
            .update_movie(
                movie_id,
                payload,
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{movie_id}",
)
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:

        MovieService(db).delete_movie(
            movie_id
        )

        return {
            "message": "Movie deleted"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )