from sqlalchemy.orm import Session
from app.modules.theatres.models import Theatre

class TheatreRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Theatre).order_by(Theatre.id.desc()).all()

    def get_by_id(self, theatre_id: int):
        return self.db.query(Theatre).filter(Theatre.id == theatre_id).first()

    def create(self, theatre: Theatre):
        self.db.add(theatre)
        self.db.commit()
        self.db.refresh(theatre)
        return theatre

    def update(self, theatre: Theatre):
        self.db.commit()
        self.db.refresh(theatre)
        return theatre

    def delete(self, theatre: Theatre):
        self.db.delete(theatre)
        self.db.commit()