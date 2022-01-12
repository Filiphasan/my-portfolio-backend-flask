from datetime import datetime
from db import db

from src.models.base import BaseModel

class ArticleTagModel(db.Model, BaseModel):
    __tablename__ = "article_tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=False)
    tag = db.relationship("TagModel", backref="article_tags", lazy=True)

    def __init__(self, article_id: int, tag_id: int):
        self.article_id = article_id
        self.tag_id = tag_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False