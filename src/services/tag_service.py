from datetime import datetime
from db import db

from src.schemas.tag_schema import TagGetSchema
from src.models.tag import TagModel
from src.utils.response import success_response, success_data_response, error_response
from src.services import ServiceMessage
from src.models.article_tag import ArticleTagModel

tag_schema = TagGetSchema()
tag_list_schema = TagGetSchema(many=True)

def list_tag():
    try:
        tags = TagModel.query.all()
        if tags:
            data = tag_list_schema.dump(tags)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_tag(id):
    try:
        tag = TagModel.query.get(id)
        if tag:
            data = tag_schema.dump(tag)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_tag(data):
    try:
        new_tag = TagModel(
            name= data["name"]
        )
        db.session.add(new_tag)
        db.session.commit()
        db.session.refresh(new_tag)
        return_data = tag_schema.dump(new_tag)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)
    
def edit_tag(id, data):
    try:
        tag = TagModel.query.get(id)
        if tag:
            tag.name= data["name"]
            tag.updated_at = datetime.now()
            db.session.commit()
            return_data = tag_schema.dump(tag)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)
    
def soft_delete_tag(id):
    try:
        tag = TagModel.query.get(id)
        if tag:
            tag.is_deleted = True
            tag.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_tag(id):
    try:
        tag = TagModel.query.get(id)
        if tag:
            article_tags = ArticleTagModel.query.filter_by(tag_id=tag.id).all()
            for article_tag in article_tags:
                db.session.delete(article_tag)
            db.session.delete(tag)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)