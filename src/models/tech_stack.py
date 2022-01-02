from datetime import datetime
from db import db

from src.models.base import BaseModel

class TechStackModel(db.Model, BaseModel):
    __tablename__ = "tech_stacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    icon = db.Column(db.String(150), nullable=False)

    def __init__(self, name: str, icon: str):
        self.name = name
        self.icon = icon
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False