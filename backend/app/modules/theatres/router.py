from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.modules.auth.dependencies import (
    require_admin,
)

from app.modules.theatres.schemas import (
    TheatreCreate,
    TheatreUpdate,
    TheatreResponse,
)

from app.modules.theatres.service import (
    TheatreService,
)

router = APIRouter(
    prefix="/theatres",
    tags=["Theatres"],
)


@router.get(
    "",
    response_model=list[TheatreResponse],
)
def get_theatres(
    db: Session = Depends(get_db),
):
    return (
        TheatreService(db)
        .get_all_theatres()
    )


@router.get(
    "/{theatre_id}",
    response_model=TheatreResponse,
)
def get_theatre(
    theatre_id: int,
    db: Session = Depends(get_db),
):
    try:

        return (
            TheatreService(db)
            .get_theatre(theatre_id)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "",
    response_model=TheatreResponse,
)
def create_theatre(
    payload: TheatreCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:

        return (
            TheatreService(db)
            .create_theatre(payload)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/{theatre_id}",
    response_model=TheatreResponse,
)
def update_theatre(
    theatre_id: int,
    payload: TheatreUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:

        return (
            TheatreService(db)
            .update_theatre(
                theatre_id,
                payload,
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{theatre_id}",
)
def delete_theatre(
    theatre_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:

        TheatreService(db).delete_theatre(
            theatre_id
        )

        return {
            "message": "Theatre deleted"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )