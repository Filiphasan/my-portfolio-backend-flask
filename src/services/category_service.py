from datetime import datetime
from db import db

from src.models.category import CategoryModel
from src.schemas.category_schema import CategoryGetSchema
from src.services import ServiceMessage
from src.utils.response import success_response, success_data_response, error_response

category_schema = CategoryGetSchema()
category_list_schema = CategoryGetSchema(many=True)

def list_category():
    try:
        categories = CategoryModel.query.all()
        if categories:
            data = category_list_schema.dump(categories)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_category(id):
    try:
        category = CategoryModel.query.get(id)
        if category:
            data = category_schema.dump(category)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_category(data):
    try:
        new_category = CategoryModel(
            name= data["name"],
            icon=data["icon"],
            is_icon_svg= data["is_icon_svg"]
        )
        db.session.add(new_category)
        db.session.commit()
        db.session.refresh(new_category)
        return_data = category_schema.dump(new_category)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_category(id, data):
    try:
        category = CategoryModel.query.get(id)
        if category:
            category.name = data["name"]
            category.icon = data["icon"]
            category.is_icon_svg = data["is_icon_svg"]
            category.updated_at = datetime.now()
            db.session.commit()
            return_data = category_schema.dump(category)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_category(id):
    try:
        category = CategoryModel.query.get(id)
        if category:
            category.is_deleted = True
            category.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_category(id):
    try:
        category = CategoryModel.query.get(id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)