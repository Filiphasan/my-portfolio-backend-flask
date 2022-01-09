from datetime import datetime
from db import db

from src.utils.response import success_response, success_data_response, error_response
from src.schemas.education_schema import EducationGetSchema
from src.services import ServiceMessage
from src.models.education import EducationModel

education_schema = EducationGetSchema()
education_list_schema = EducationGetSchema(many=True)

def list_education():
    try:
        educations = EducationModel.query.filter_by(is_deleted=False).all()
        if educations:
            data = education_list_schema.dump(educations)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_education(id):
    try:
        education = EducationModel.query.filter_by(id=id).first()
        if education and not education.is_deleted:
            data = education_schema.dump(education)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_education(data):
    try:
        new_education = EducationModel(
            institution= data["institution"],
            title= data["title"],
            begin_date= data["begin_date"],
            end_date= data["end_date"],
            avarage= data["avarage"],
            description= data["description"]
        )
        db.session.add(new_education)
        db.session.commit()
        db.session.refresh(new_education)
        retutn_data = education_schema.dump(new_education)
        return success_data_response(retutn_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_education(id, data):
    try:
        education = EducationModel.query.filter_by(id=id).first()
        if education and not education.is_deleted:
            education.institution = data["institution"]
            education.title = data["title"]
            education.begin_date = data["begin_date"]
            education.end_date = data["end_date"]
            education.avarage = data["avarage"]
            education.description= data["description"]
            education.updated_at = datetime.now()
            db.session.commit()
            return_data = education_schema.dump(education)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_education(id):
    try:
        education = EducationModel.query.filter_by(id=id).first()
        if education and not education.is_deleted:
            education.is_deleted = True
            education.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_education(id):
    try:
        education = EducationModel.query.filter_by(id=id).first()
        if education:
            db.session.delete(education)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)     


