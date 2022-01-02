from datetime import datetime
from db import db

from src.models.base import BaseModel

class SkillModel(db.Model, BaseModel):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    skill_level = db.Column(db.Integer, nullable=True)
    image_path = db.Column(db.String(250), nullable=True)
    bg_color_from = db.Column(db.String(20), nullable=True)
    bg_color_to = db.Column(db.String(20), nullable=True)

    def __init__(self, name: str, skill_level: int, image_path: str, bg_color_from: str, bg_color_to: str):
        self.name = name
        self.skill_level = skill_level
        self.image_path = image_path
        self.bg_color_from = bg_color_from
        self.bg_color_to = bg_color_to
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
    