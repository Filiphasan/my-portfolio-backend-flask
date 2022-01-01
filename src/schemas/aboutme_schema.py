from marshmallow import Schema, fields, validate

from src.schemas.messages.about_me import AboutMeMessage

class AboutMeSchema(Schema):
    id = fields.String(required=False)
    full_name = fields.String(required=True, 
        validate=validate.Length(5, 70, error=AboutMeMessage.FULL_NAME_LEN_MSG), 
        error_messages={"required":AboutMeMessage.FULL_NAME_REQ_MSG})
    job_title = fields.String(required=True, 
        validate=validate.Length(5, 120, error=AboutMeMessage.JOB_TITLE_LEN_MSG), 
        error_messages={"required":AboutMeMessage.JOB_TITLE_REQ_MSG})
    short_desc = fields.String(required=True, 
        validate=validate.Length(40, 340, error=AboutMeMessage.JOB_TITLE_LEN_MSG), 
        error_messages={"required":AboutMeMessage.JOB_TITLE_REQ_MSG})
    profile_photo = fields.Raw(required=True, error_messages={"required":AboutMeMessage.PROFILE_PHOTO_REQ_MSG})
    birth_date = fields.Date("%d.%m.%Y", error_messages={"format":AboutMeMessage.BIRTH_DATE_FORMAT_MSG})
    phone_number = fields.String(required=True, 
        validate=validate.Length(9, 20, error=AboutMeMessage.PHONE_NUMBER_LEN_MSG), error_messages={"required":AboutMeMessage.PHONE_NUMBER_REQ_MSG})
    email = fields.String(
        required=True, 
        validate=[validate.Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", error=AboutMeMessage.MAIL_REGEX_MSG),
            validate.Length(10,100,error=AboutMeMessage.MAIL_LEN_MSG)], 
        error_messages={"required":AboutMeMessage.MAIL_REQ_MSG})
    short_adress = fields.String(required=True, 
        validate=validate.Length(10, 50, error=AboutMeMessage.SHORT_ADRESS_LEN_MSG), 
        error_messages={"required":AboutMeMessage.SHORT_ADRESS_REQ_MSG})

class AboutMeGetSchema(Schema):
    id = fields.String()
    full_name = fields.String()
    job_title = fields.String()
    short_desc = fields.String()
    birth_date = fields.String()
    phone_number = fields.String()
    email = fields.String()
    short_adress = fields.String()