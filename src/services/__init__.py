server_error_obj = {
    'status':'error',
    'message':'Internal Server Error!'
}
not_found_obj = {
    'status':'error',
    'message':'Not Found!'
}
delete_success_obj = {
    'status':'success',
    'message':'Deletion Successful.'
}
email_already_exist_obj = {
    'status':'error',
    'message':'Email already exist!'
}
email_not_confirmed_obj = {
    'status':'error',
    'message':'Email not confirmed!'
}
password_wrong_obj = {
    'status':'error',
    'message':'Email or Password is wrong!'
}
password_change_success_obj = {
    'status':'success',
    'message':'Successfully edit password.'
}

class ServiceMessage:
    SERVER_ERROR = "Internal Server Error!"
    NOT_FOUND = "Not Found!"
    DELETE_SUCCESS = "Deletion Successful."
    MAIL_ALREADY_EXIST = "Email already exist!"
    MAIL_NOT_CONFIRMED = "Email not confirmed!"
    MAIL_OR_PASSWORD_WRONG = "Email or Password is wrong!"
    PASSWORD_UPDATE_SUCCESS = "Successfully edit password."