from datetime import datetime
from db import db

from src.models.base import BaseModel

class UserRolesModel(db.Model, BaseModel):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #User Relations
    user_id = db.Column(db.String(128), db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UsersModel", backref="user_roles")
    role = db.Column(db.String(30), nullable=False)

    def __init__(self, user_id: str, role: str):
        self.user_id = user_id
        self.role = role
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False