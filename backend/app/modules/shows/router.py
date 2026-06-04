from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.modules.auth.dependencies import (
    require_admin,
)

from app.modules.shows.schemas import (
    ShowCreate,
    ShowUpdate,
    ShowResponse,
)

from app.modules.shows.service import (
    ShowService,
)

router = APIRouter(
    prefix="/shows",
    tags=["Shows"],
)


@router.get(
    "",
    response_model=list[ShowResponse],
)
def get_shows(
    db: Session = Depends(get_db),
):
    return (
        ShowService(db)
        .get_all_shows()
    )


@router.get(
    "/{show_id}",
    response_model=ShowResponse,
)
def get_show(
    show_id: int,
    db: Session = Depends(get_db),
):
    try:
        return (
            ShowService(db)
            .get_show(show_id)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "",
    response_model=ShowResponse,
)
def create_show(
    payload: ShowCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:
        return (
            ShowService(db)
            .create_show(payload)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/{show_id}",
    response_model=ShowResponse,
)
def update_show(
    show_id: int,
    payload: ShowUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:
        return (
            ShowService(db)
            .update_show(
                show_id,
                payload,
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{show_id}",
)
def delete_show(
    show_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    try:

        ShowService(db).delete_show(
            show_id
        )

        return {
            "message": "Show deleted"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )