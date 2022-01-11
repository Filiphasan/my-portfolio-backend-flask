from datetime import datetime
from db import db

from src.schemas.experience_schema import ExperienceGetSchema
from src.models.experience import ExperienceModel
from src.models.experience_stack import ExperienceStackModel
from src.services import ServiceMessage
from src.utils.response import success_response, success_data_response, error_response

experience_schema = ExperienceGetSchema()
experience_list_schema = ExperienceGetSchema(many=True)

def list_experience():
    try:
        experiences = ExperienceModel.query.filter_by(is_deleted=False).all()
        if experiences:
            data = experience_list_schema.dump(experiences)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_experience(id):
    try:
        experience = ExperienceModel.query.filter_by(id=id).first()
        if experience and not experience.is_deleted:
            data = experience_schema.dump(experience)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_experience(data):
    try:
        new_experience = ExperienceModel(
            title= data["title"],
            company= data["company"],
            start_date= data["start_date"],
            end_date= data["end_date"],
            description= data["description"]
        )
        db.session.add(new_experience)
        for stack_id in data["experience_stacks"]:
            new_experience.experience_stacks.append(ExperienceStackModel(experience_id=new_experience.id,tech_stack_id=stack_id))
        db.session.commit()
        db.session.refresh(new_experience)
        return_data = experience_schema.dump(new_experience)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_experience(id,data):
    try:
        experience = ExperienceModel.query.filter_by(id=id).first()
        if experience:
            for stack in experience.experience_stacks:
                db.session.delete(stack)
                # experience.experience_stacks.remove(stack)
            experience.title = data["title"]
            experience.company = data["company"]
            experience.start_date = data["start_date"]
            experience.end_date = data["end_date"]
            experience.description = data["description"]
            for stack_id in data["experience_stacks"]:
                experience.experience_stacks.append(ExperienceStackModel(experience_id=id, tech_stack_id=stack_id))
            db.session.commit()
            db.session.refresh(experience)
            return_data = experience_schema.dump(experience)
            print(return_data)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_experience(id):
    try:
        experience = ExperienceModel.query.filter_by(id=id).first()
        if experience:
            for stack in experience.experience_stacks:
                db.session.delete(stack)
            experience.is_deleted = True
            experience.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_experience(id):
    try:
        experience = ExperienceModel.query.filter_by(id=id).first()
        if experience:
            for stack in experience.experience_stacks:
                db.session.delete(stack)
            db.session.delete(experience)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)
