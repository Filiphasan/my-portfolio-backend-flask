def success_data_response(data, code: int):
    return {
        "status":"success",
        "status-code":code,
        "data":data
    }, code

def success_data_response_with_pagination(data, code: int, page: int, item_count: int, item_count_per_page: int, page_count: int):
    return {
        "status":"success",
        "status-code": code,
        "data": data,
        "page_number": page,
        "count": item_count,
        "item_count_per_page": item_count_per_page,
        "page_count": page_count 
    }

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