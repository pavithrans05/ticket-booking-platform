from fastapi import FastAPI

from app.common.health import router as health_router
from app.modules.auth.router import router as auth_router
from app.modules.movies.router import router as movies_router

from app.core.config import settings

from app.modules.shows.router import router as shows_router
from app.modules.theatres.router import (
    router as theatres_router,
)
app = FastAPI(
    title=settings.APP_NAME,
)


app.include_router(
    health_router
)

app.include_router(
    auth_router
)

app.include_router(
    movies_router
)

app.include_router(
    shows_router
)

app.include_router(
    theatres_router
)

@app.get("/")
def root():
    return {
        "message": "Booking Platform API"
    }