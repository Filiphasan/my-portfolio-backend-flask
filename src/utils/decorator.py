from ast import List
from functools import wraps
from flask import request
import jwt
import os

from src.utils.response import error_response

secret_key = os.environ.get("SECRET_KEY", 'application_secret_key')

TOKEN_NOT_FOUND = "Token not found!"
INVALID_TOKEN = "Invalid token!"
NOT_AUTH_AREA = "You don't have access this area!"

def token_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if 'Authorization' in request.headers:
            bearer_token = request.headers['Authorization']
            tokenArr = bearer_token.split(" ")
            token = tokenArr[1]
            if not token:
                return error_response(TOKEN_NOT_FOUND, 401)
            try:
                data = jwt.decode(
                    token, secret_key, algorithms="HS256")
            except:
                return error_response(INVALID_TOKEN, 403)
        else:
            return error_response(TOKEN_NOT_FOUND, 401)
        return func(*args, **kwargs)
    return wrapped

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if 'Authorization' in request.headers:
                bearer_token = request.headers['Authorization']
                tokenArr = bearer_token.split(" ")
                token = tokenArr[1]
                if not token:
                    return error_response(TOKEN_NOT_FOUND, 401)
                try:
                    data = jwt.decode(
                        token, secret_key, algorithms="HS256")
                    user_role = data["role"]
                    if user_role not in roles:                     
                        return error_response(NOT_AUTH_AREA, 401)
                except:
                    return error_response(INVALID_TOKEN, 403)
            else:   
                return error_response(TOKEN_NOT_FOUND, 401)
            return func(*args, **kwargs)
        return wrapped
    return decorator