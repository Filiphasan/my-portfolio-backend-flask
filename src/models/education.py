from datetime import datetime
from db import db

from src.models.base import BaseModel

class EducationModel(db.Model, BaseModel):
    __tablename__ = "educations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    institution = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    begin_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    avarage = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(400), nullable=False)

    def __init__(self, institution: str, title: str, begin_date: str, end_date: str, avarage: str, description: str):
        self.institution = institution
        self.title = title
        self.begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.avarage = avarage
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False