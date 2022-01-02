def success_data_response(data, code: int):
    return {
        "status":"success",
        "status-code":code,
        "data":data
    }, code

def success_token_response(token: str, code: int):
    return {
        "status":"success",
        "status-code": code,
        "access-token": token
    }, code

def success_response(message: str, code: int):
    return {
        "status":"success",
        "status-code": code,
        "message": message
    }, code

def error_response(message: str, code: int):
    return {
        "status":"error",
        "status-code":code,
        "message":message
    }, code