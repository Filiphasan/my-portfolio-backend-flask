from marshmallow import Schema, fields, validate
from src.schemas.messages.interest import InterestMessage

class InterestAddEditSchema(Schema):
    title = fields.String(required=True,
        validate=validate.Length(min=20, max=240, error=InterestMessage.TITLE_LEN_MSG),
        error_messages={"required":InterestMessage.TITLE_REQ_MSG})

class InterestGetSchema(Schema):
    id = fields.Integer()
    title = fields.String()