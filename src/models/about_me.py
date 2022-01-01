from db import db
from datetime import datetime

from src.models.base import BaseModel

class AboutMeModel(db.Model, BaseModel):
    __tablename__ = 'about_me'

    id = db.Column(db.String(128), primary_key=True)
    full_name = db.Column(db.String(70), nullable=False)
    job_title = db.Column(db.String(120), nullable=False)
    short_desc = db.Column(db.String(340), nullable=False)
    profile_photo = db.Column(db.String(250), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    short_adress = db.Column(db.String(50), nullable=False)

    def __init__(self, id: str, full_name: str, job_title: str, short_desc: str, profile_photo: str, birth_date: str, phone_number: str, email: str, short_adress: str):
        self.id = id
        self.full_name = full_name
        self.job_title = job_title
        self.short_desc = short_desc
        self.profile_photo = profile_photo
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        self.phone_number = phone_number
        self.email = email
        self.short_adress = short_adress
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False