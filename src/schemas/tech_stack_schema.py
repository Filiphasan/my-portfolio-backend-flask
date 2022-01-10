from marshmallow import Schema, fields, validate
from src.schemas.messages.tech_stack import TechStackMessage

class TechStackAddEditSchema(Schema):
    name = fields.String(required=True,
        validate=validate.Length(1, 60, error=TechStackMessage.NAME_LEN_MSG),
        error_messages={"required":TechStackMessage.NAME_REQ_MSG})
    icon = fields.String(required=True,
        validate=validate.Length(min=10, error=TechStackMessage.ICON_LEN_MSG),
        error_messages={"required":TechStackMessage.ICON_REQ_MSG})
    is_icon_devicon = fields.Boolean(truthy={1, "1", "True", "true", True},falsy={0, "0", "False", "false", False},
        required=True,
        error_messages={"required":TechStackMessage.IS_ICON_DEV_REQ_MSG, "invalid":TechStackMessage.IS_ICON_DEV_INVALID_MSG})

class TechStachGetSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    icon = fields.String()
    is_icon_devicon = fields.Boolean()
    created_at = fields.DateTime(format="%Y-%m-%d %H:%M")
    updated_at = fields.DateTime(format="%Y-%m-%d %H:%M")