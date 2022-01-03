from datetime import datetime
from db import db

from src.models.base import BaseModel

class InterestModel(db.Model, BaseModel):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(240), nullable=False)

    def __init__(self, title: str):
        self.title = title
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False