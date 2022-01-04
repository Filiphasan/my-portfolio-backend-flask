from datetime import datetime
from db import db

from src.models.base import BaseModel

class CommentModel(db.Model, BaseModel):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    full_name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(400), nullable=False)

    def __init__(self, article_id: int, full_name: str, mail: str, comment: str):
        self.article_id = article_id
        self.full_name = full_name
        self.mail = mail
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False