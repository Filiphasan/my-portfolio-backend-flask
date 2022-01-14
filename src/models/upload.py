from datetime import datetime
from db import db
from src.models.base import BaseModel

class UploadModel(db.Model, BaseModel):
    __tablename__ = "uploads"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upload_for = db.Column(db.String(30), nullable=True)
    upload_for_id = db.Column(db.String(128), nullable=True)
    filename = db.Column(db.String(60), nullable=False)
    file_path = db.Column(db.String(240), nullable=False)

    def __init__(self, filename: str, file_path: str, upload_for, upload_for_id):
        self.upload_for = upload_for
        self.upload_for_id = upload_for_id
        self.filename = filename
        self.file_path = file_path
        self.is_deleted = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()