from marshmallow import Schema, fields, validate
from src.schemas.messages.contact import ContactMessage

class ContactAddSchema(Schema):
    first_name = fields.String(required=True,
        validate=validate.Length(2, 35, error=ContactMessage.FIRST_NAME_LEN_MSG),
        error_messages={"required":ContactMessage.FIRST_NAME_REQ_MSG})
    last_name = fields.String(required=True,
        validate=validate.Length(2, 35, error=ContactMessage.LAST_NAME_LEN_MSG),
        error_messages={"required":ContactMessage.LAST_NAME_REQ_MSG})
    mail = fields.Email(required=True,
        error_messages={"required":ContactMessage.MAIL_REQ_MSG, "invalid":ContactMessage.MAIL_FORMAT_MSG})
    subject = fields.String(required=True,
        validate=validate.Length(5, 100, error=ContactMessage.SUBJ_LEN_MSG),
        error_messages={"required":ContactMessage.SUBJ_REQ_MSG})
    message = fields.String(required=True,
        validate=validate.Length(10, 500, error=ContactMessage.MESSAGE_LEN_MSG),
        error_messages={"required":ContactMessage.MESSAGE_REQ_MSG})

class ContactGetSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    mail = fields.String()
    subject = fields.String()
    message = fields.String()