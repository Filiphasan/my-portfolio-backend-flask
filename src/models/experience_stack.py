from datetime import datetime
from db import db

from src.models.base import BaseModel

class ExperienceStackModel(db.Model, BaseModel):
    __tablename__ = "experience_stacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #Experience Relation
    experience_id = db.Column(db.Integer, db.ForeignKey("experiences.id"), nullable=False)
    experience = db.relationship("ExperienceModel", backref="experience_stacks")
    #Tech Stack Relation
    tech_stack_id = db.Column(db.Integer, db.ForeignKey("tech_stacks.id"), nullable=False)
    tech_stack = db.relationship("TechStackModel", backref="experience_stacks")
    
    def __init__(self, experience_id: int, tech_stack_id: int):
        self.experience_id = experience_id
        self.tech_stack_id = tech_stack_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False