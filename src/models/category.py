from datetime import datetime
from db import db

from src.models.base import BaseModel

class CategoryModel(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(12000), nullable=False)
    is_icon_svg = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name: str, icon: str, is_icon_svg: bool):
        self.icon =icon
        self.name = name
        self.is_icon_svg = is_icon_svg
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False