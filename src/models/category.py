from datetime import datetime
from db import db

from src.models.base import BaseModel

class CategoryModel(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icon = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, icon: str, name: str):
        self.icon =icon
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False