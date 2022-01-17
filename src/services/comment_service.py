from db import db

from src.services import ServiceMessage
from src.models.comment import CommentModel
from src.utils.response import success_response, error_response

def add_comment(data):
    try:
        new_comment = CommentModel(
            article_id= data["article_id"],
            full_name= data["full_name"],
            mail= data["mail"],
            comment= data["comment"]
        )
        db.session.add(new_comment)
        db.session.commit()
        return success_response("Comment successfully added.", 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_comment(id):
    try:
        comment = CommentModel.query.get(id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)