from datetime import datetime
from db import db

from src.models.base import BaseModel

class ProjectModel(db.Model, BaseModel):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    has_repo = db.Column(db.Boolean, default=True, nullable=False)
    repo_url = db.Column(db.String(240), nullable=True)
    has_demo = db.Column(db.Boolean, default=True, nullable=False)
    demo_url = db.Column(db.String(240), nullable=True)
    project_stacks = db.relationship("ProjectStackModel", backref='projects', lazy=True)

    def __init__(self, name: str, description: str, release_date: str, has_repo: bool, repo_url, has_demo: str, demo_url):
        self.name = name
        self.description = description
        self.release_date = datetime.strptime(release_date, "%Y-%m-%d")
        self.has_repo = has_repo
        self.repo_url = repo_url
        self.has_demo = has_demo
        self.demo_url = demo_url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False