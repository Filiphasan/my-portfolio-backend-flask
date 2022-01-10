from datetime import datetime
from db import db

from src.schemas.tech_stack_schema import TechStachGetSchema
from src.models.tech_stack import TechStackModel
from src.utils.response import success_response, success_data_response, error_response
from src.services import ServiceMessage

tech_stack_schema = TechStachGetSchema()
tech_stack_list_schema = TechStachGetSchema(many=True)

def list_tech_stack():
    try:
        tech_stacks = TechStackModel.query.filter_by(is_deleted=False).all()
        if tech_stacks:
            data = tech_stack_list_schema.dump(tech_stacks)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)


def get_tech_stack(id):
    try:
        tech_stack = TechStackModel.query.filter_by(id=id).first()
        if tech_stack:
            data = tech_stack_schema.dump(tech_stack)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_tech_stack(data):
    try:
        new_tech_stack = TechStackModel(
            name= data["name"],
            icon= data["icon"],
            is_icon_devicon= data["is_icon_devicon"]
        )
        db.session.add(new_tech_stack)
        db.session.commit()
        db.session.refresh(new_tech_stack)
        return_data = tech_stack_schema.dump(new_tech_stack)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_tech_stack(id, data):
    try:
        tech_stack = TechStackModel.query.filter_by(id=id).first()
        if tech_stack:
            tech_stack.name = data["name"]
            tech_stack.icon = data["icon"]
            tech_stack.is_icon_devicon = data["is_icon_devicon"]
            tech_stack.updated_at = datetime.now()
            db.session.commit()
            return_data = tech_stack_schema.dump(tech_stack)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_tech_stack(id):
    try:
        tech_stack = TechStackModel.query.filter_by(id=id).first()
        if tech_stack:
            tech_stack.is_deleted = True
            tech_stack.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_tech_stack(id):
    try:
        tech_stack = TechStackModel.query.filter_by(id=id).first()
        if tech_stack:
            db.session.delete(tech_stack)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)