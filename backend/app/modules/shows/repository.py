from sqlalchemy.orm import Session

from app.modules.shows.models import Show


class ShowRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_all(self):
        return (
            self.db.query(Show)
            .order_by(Show.id.desc())
            .all()
        )

    def get_by_id(
        self,
        show_id: int,
    ):
        return (
            self.db.query(Show)
            .filter(Show.id == show_id)
            .first()
        )

    def create(
        self,
        show: Show,
    ):
        self.db.add(show)
        self.db.commit()
        self.db.refresh(show)

        return show

    def update(
        self,
        show: Show,
    ):
        self.db.commit()
        self.db.refresh(show)

        return show

    def delete(
        self,
        show: Show,
    ):
        self.db.delete(show)
        self.db.commit()