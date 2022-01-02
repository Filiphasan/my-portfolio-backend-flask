from datetime import datetime
from db import db

from src.models.base import BaseModel

class EducationModel(db.Model, BaseModel):
    __tablename__ = "educations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    institution = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    avarage = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(400), nullable=False)

    def __init__(self, institution: str, title: str, duration: str, avarage: str, description: str):
        self.institution = institution
        self.title = title
        self.duration = duration
        self.avarage = avarage
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False