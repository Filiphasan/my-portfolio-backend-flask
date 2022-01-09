from datetime import datetime
from db import db

from src.models.skill import SkillModel
from src.schemas.skill_schema import SkillGetSchema
from src.utils.response import error_response, success_data_response, success_response
from src.services import ServiceMessage

skill_schema = SkillGetSchema()
skill_list_schema = SkillGetSchema(many=True)

def list_skills():
    try:
        skills = SkillModel.query.filter_by(is_deleted=False).all()
        if skills:
            data = skill_list_schema.dump(skills)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_skill(id):
    try:
        skill = SkillModel.query.filter_by(id=id).first()
        if skill and not skill.is_deleted:
            data = skill_schema.dump(skill)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_skill(data):
    try:
        new_skill = SkillModel(
            name= data["name"],
            icon= data["icon"],
            is_icon_svg= data["is_icon_svg"]
        )
        db.session.add(new_skill)
        db.session.commit()
        db.session.refresh(new_skill)
        return_data = skill_schema.dump(new_skill)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def update_skill(id, data):
    try:
        skill = SkillModel.query.filter_by(id=id).first()
        if skill:
            skill.name = data["name"]
            skill.icon = data["icon"]
            skill.is_icon_svg = data["is_icon_svg"]
            skill.updated_at = datetime.now()
            db.session.commit()
            return_data = skill_schema.dump(skill)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete(id):
    try:
        skill = SkillModel.query.filter_by(id=id).first()
        if skill:
            skill.is_deleted = True
            skill.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete(id):
    try:
        skill = SkillModel.query.filter_by(id=id).first()
        if skill:
            db.session.delete(skill)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

