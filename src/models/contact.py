from datetime import datetime
from db import db

from src.models.base import BaseModel

class ContactModel(db.Model, BaseModel):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    mail =db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __init__(self, first_name: str, last_name: str, mail: str, subject: str, message: str):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.subject = subject
        self.message = message
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False