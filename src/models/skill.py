from datetime import datetime
from db import db

from src.models.base import BaseModel

class SkillModel(db.Model, BaseModel):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    skill_level = db.Column(db.Integer, nullable=True)
    icon = db.Column(db.String(10000), nullable=False)
    is_icon_svg = db.Column(db.Boolean, default=False, nullable=False)
    bg_color_from = db.Column(db.String(20), nullable=True)
    bg_color_to = db.Column(db.String(20), nullable=True)

    def __init__(self, name: str, icon: str, is_icon_svg: bool):
        self.name = name
        self.icon = icon
        self.is_icon_svg = is_icon_svg
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
    