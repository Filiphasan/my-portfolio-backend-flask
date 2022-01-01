from datetime import datetime
from db import db

from src.models.about_me import AboutMeModel
from src.schemas.aboutme_schema import AboutMeGetSchema
from src.services import server_error_obj, not_found_obj

aboutmes_schema = AboutMeGetSchema(many=True)
aboutme_schema = AboutMeGetSchema()

def list_aboutme():
    try:
        about_mes = AboutMeModel.query.filter_by(is_deleted=False).all()
        if about_mes:
            return aboutmes_schema.dump(about_mes), 200
        else:
            return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def get_about_me(id: str):
    try:
        about_me = AboutMeModel.query.get(id)
        if about_me:
            return aboutme_schema.dump(about_me), 200
        else:
            return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

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
        else: 
            return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

