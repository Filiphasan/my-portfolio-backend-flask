from datetime import date, datetime
from db import db

from src.models.base import BaseModel

class ExperienceModel(db.Model, BaseModel):
    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    experience_stacks = db.relationship('ExperienceStackModel', backref='experiences', lazy=True)

    def __init__(self, title: str, company: str, start_date: date, end_date: date, description: str):
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
