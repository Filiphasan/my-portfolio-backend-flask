from db import db

from src.schemas.contact_schema import ContactGetSchema
from src.utils.response import success_response, success_data_response, error_response
from src.services import ServiceMessage
from src.models.contact import ContactModel

contact_schema = ContactGetSchema()
contact_list_schema = ContactGetSchema(many=True)

def list_contact():
    try:
        contacts = ContactModel.query.all()
        if contacts:
            data = contact_list_schema.dump(contacts)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_contact(id):
    try:
        contact = ContactModel.query.filter_by(id=id).first()
        if contact:
            data = contact_schema.dump(contact)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_contact(data):
    try:
        new_contact = ContactModel(
            first_name= data["first_name"],
            last_name= data["last_name"],
            mail= data["mail"],
            subject= data["subject"],
            message= data["message"]
        )
        db.session.add(new_contact)
        db.session.commit()
        return success_response(ServiceMessage.MSG_SUCCESS_ADD, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_contact(id):
    try:
        contact = ContactModel.query.filter_by(id=id).first()
        if contact:
            db.session.delete(contact)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

