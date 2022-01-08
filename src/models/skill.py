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

    def __init__(self, name: str, skill_level: int, icon: str, bg_color_from: str, bg_color_to: str):
        self.name = name
        self.skill_level = skill_level
        self.icon = icon
        self.bg_color_from = bg_color_from
        self.bg_color_to = bg_color_to
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
    