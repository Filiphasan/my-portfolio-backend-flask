from datetime import datetime
from db import db
from src.models.base import BaseModel

class ProjectStackModel(db.Model, BaseModel):
    __tablename__ = "project_stacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Project Realtion
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    project = db.relationship("ProjectModel", backref="project_stacks")
    #Tech Stack Relation
    tech_stack_id = db.Column(db.Integer, db.ForeignKey("tech_stacks.id"), nullable=False)
    tech_stack = db.relationship("TechStackModel", backref="project_stacks")

    def __init__(self, project_id: int, tech_stack_id: int):
        self.project_id = project_id
        self.tech_stack_id = tech_stack_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False