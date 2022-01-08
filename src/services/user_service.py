from os import error
import uuid
import datetime
import hashlib

from src.models.users import UsersModel
from src.schemas.user_schemas import UserGetSchema
from src.services import ServiceMessage
from src.utils.response import success_data_response, error_response, success_response

from db import db

user_schema = UserGetSchema()
users_schema = UserGetSchema(many=True)


def save_new_user(user_data):
    try:
        user = UsersModel.query.filter_by(email=user_data['email']).first()
        if user:
            return error_response(ServiceMessage.MAIL_ALREADY_EXIST, 400)
        else:
            password = user_data['password']
            new_user = UsersModel(
                id = str(uuid.uuid4()),
                first_name= user_data['first_name'],
                last_name= user_data['last_name'],
                email= user_data['email'],
                username= user_data['username'],
                password_hash= hashlib.md5(password.encode()).hexdigest()
            )
            db.session.add(new_user)
            db.session.commit()
            db.session.refresh(new_user)
            data = user_schema.dump(new_user)
            return success_data_response(data, 201)
    except:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_all_users(is_deleted=False, email_confirmed=True):
    try:
        users = UsersModel.query.filter_by(is_deleted=is_deleted, email_confirmed=email_confirmed).all()
        if users:
            data = users_schema.dump(users)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_user_id(user_id : str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            data = user_schema.dump(user)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as err:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def get_user(type: str, data: str):
    try:
        if type=="mail":
            user = UsersModel.query.filter_by(email=data).first()
            if user:
                data = user_schema.dump(user)
                return success_data_response(data, 200)
            else:
                return error_response(ServiceMessage.NOT_FOUND, 404)
        else:
            user = UsersModel.query.filter_by(username=data).first()
            if user:
                data = user_schema.dump(user)
                return success_data_response(data, 200)
            else:
                return error_response(ServiceMessage.NOT_FOUND, 404)
    except:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def update_user(user_data, id: str):
    try:
        user = UsersModel.query.get(id)
        if not user:
            return error_response(ServiceMessage.NOT_FOUND, 404)
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.full_name = user_data["first_name"] + " " + user_data["last_name"]
        user.username = user_data["username"]
        user.email = user_data["email"]
        user.updated_at = datetime.datetime.utcnow()
        db.session.commit()
        data = user_schema.dump(user)
        return success_data_response(data, 200)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_user_password(id: str, data):
    try:
        new_password = data["new_password"]
        old_password = data["old_password"]
        user = UsersModel.query.get(id)
        old_pw_hash = hashlib.md5(old_password.encode()).hexdigest()
        if user:
            if user.password != old_pw_hash:
                return error_response(ServiceMessage.MAIL_OR_PASSWORD_WRONG, 400)
            new_pw_hash = hashlib.md5(new_password.encode()).hexdigest()
            user.password = new_pw_hash
            user.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return success_response(ServiceMessage.PASSWORD_UPDATE_SUCCESS, 200)
        return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            user.is_deleted = True
            user.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        return error_response(ServiceMessage.NOT_FOUND, 404)
    except:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def hard_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        return error_response(ServiceMessage.NOT_FOUND, 404)
    except:
        return error_response(ServiceMessage.SERVER_ERROR, 500)
