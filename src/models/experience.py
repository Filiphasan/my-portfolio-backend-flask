from datetime import datetime
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
    #Experience Stack Many 
    experience_stacks = db.relationship('ExperienceStackModel', backref='experiences') #I don't need this, just this is easy way for data join.

    def __init__(self, title: str, company: str, start_date: str, end_date: str, description: str):
        self.title = title
        self.company = company
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y").date()
        self.end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
