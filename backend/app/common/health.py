from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import engine

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    mysql_status = "unhealthy"

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        mysql_status = "healthy"

    except Exception:
        mysql_status = "unhealthy"

    return {
        "api": "healthy",
        "mysql": mysql_status,
    }