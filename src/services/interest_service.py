from datetime import datetime
from db import db

from src.schemas.interest_schema import InterestGetSchema
from src.utils.response import success_response, success_data_response, error_response
from src.services import ServiceMessage
from src.models.interest import InterestModel

interst_schema = InterestGetSchema()
interst_list_schema = InterestGetSchema(many=True)

def list_interest():
    try:
        interests = InterestModel.query.all()
        if interests:
            data =interst_list_schema.dump(interests)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def list_interest_non_delete():
    try:
        interests = InterestModel.query.filter_by(is_deleted=False).all()
        if interests:
            data =interst_list_schema.dump(interests)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_interest(id):
    try:
        interest = InterestModel.query.filter_by(id=id).first()
        if interest:
            data = interst_schema.dump(interest)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_interest(data):
    try:
        new_interest = InterestModel(
            title= data["title"]
        )
        db.session.add(new_interest)
        db.session.commit()
        db.session.refresh(new_interest)
        return_data = interst_schema.dump(new_interest)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_interest(id, data):
    try:
        interest = InterestModel.query.filter_by(id=id).first()
        if interest:
            interest.title = data["title"]
            interest.updated_at = datetime.now()
            db.session.commit()
            return_data = interst_schema.dump(interest)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_interest(id):
    try:
        interest = InterestModel.query.filter_by(id=id).first()
        if interest:
            interest.is_deleted = True
            interest.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_interest(id):
    try:
        interest = InterestModel.query.filter_by(id=id).first()
        if interest:
            db.session.delete(interest)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)