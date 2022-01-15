from typing import Dict
import jwt
import datetime
import hashlib
import os

from src.models.users import UsersModel
from src.services import ServiceMessage
from src.utils.response import success_token_response, error_response

secret_key = os.environ.get("SECRET_KEY", 'application_secret_key')

def login(data):
    try:
        email = data['email']
        password = data["password"]
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user = UsersModel.query.filter_by(email=email, password=password_hash).first()
        if user:
            if not user.email_confirmed:
                return error_response(ServiceMessage.MAIL_NOT_CONFIRMED, 401)
            else:
                token = create_token(user=user)
                return success_token_response(token, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def create_token(user: UsersModel):
    token = jwt.encode({
        'sub': user.id,
        'exp': datetime.datetime.now()+datetime.timedelta(minutes=120),
        'iat': datetime.datetime.now(),
        'role': user.role
    },secret_key, algorithm='HS256')
    return token

