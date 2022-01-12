from datetime import datetime
from db import db

from src.models.base import BaseModel

class ArticleModel(db.Model, BaseModel):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    thumbnail = db.Column(db.String(240), nullable=True)
    short_content = db.Column(db.String(400), nullable=False)
    content = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category = db.relationship("CategoryModel", backref="articles", lazy=True)
    views_count = db.Column(db.Integer, default=0, nullable=False)
    comment_count = db.Column(db.Integer, default=0, nullable=False)
    comments = db.relationship("CommentModel", backref="articles", lazy="joined")
    tags = db.relationship("ArticleTagModel", backref="articles", lazy=True)
    seo_tags = db.Column(db.String(150), default="Software, Flask, Python, .Net Core, Web, Developer, JavaScript, React, Asp.Net, HTML5, CSS3, Web Development, Mobile, React Native", nullable=False)
    seo_description = db.Column(db.String(150), default="", nullable=False)

    def __init__(self, title: str, thumbnail: str, short_content: str, content: str, category_id: int, seo_tags: str, seo_description: str):
        self.title = title
        self.thumbnail = thumbnail
        self.short_content = short_content
        self.content = content
        self.category_id = category_id
        self.views_count = 0
        self.seo_tags = seo_tags
        self.seo_description = seo_description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
