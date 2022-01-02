from datetime import datetime
from db import db

from src.models.about_me import AboutMeModel
from src.schemas.aboutme_schema import AboutMeGetSchema
from src.services import ServiceMessage
from src.utils.response import success_data_response, error_response

aboutmes_schema = AboutMeGetSchema(many=True)
aboutme_schema = AboutMeGetSchema()

def list_aboutme():
    try:
        about_mes = AboutMeModel.query.filter_by(is_deleted=False).all()
        if about_mes:
            data = aboutmes_schema.dump(about_mes)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_about_me(id: str):
    try:
        about_me = AboutMeModel.query.get(id)
        if about_me:
            data = aboutme_schema.dump(about_me)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_about_me(id: str, data):
    try:
        about_me = AboutMeModel.query.get(id)
        if about_me:
            about_me.full_name = data["full_name"]
            about_me.job_title = data["job_title"]
            about_me.short_desc = data["short_desc"]
            about_me.birth_date = data["birth_date"]
            about_me.phone_number = data["phone_number"]
            about_me.email = data["email"]
            about_me.short_adress = data["short_adress"]
            about_me.updated_at = datetime.now()
            db.session.commit()
            data = aboutme_schema.dump(about_me)
            return success_data_response(data, 200)
        else: 
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

