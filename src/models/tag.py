from datetime import datetime
from db import db

from src.models.base import BaseModel

class TagModel(db.Model, BaseModel):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(20), nullable=False)

    def __init__(self, tag: str):
        self.tag = tag
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False