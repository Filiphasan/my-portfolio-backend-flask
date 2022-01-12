from marshmallow import Schema, fields, validate
from src.schemas.messages.category import CategoryMessage

class CategoryAddEditSchema(Schema):
    name = fields.String(required=True,
        validate=validate.Length(max=50, error=CategoryMessage.NAME_LEN_MSG),
        error_messages={"required":CategoryMessage.NAME_REQ_MSG})
    icon = fields.String(required=True,
        validate=validate.Length(min=5, error=CategoryMessage.ICON_LEN_MSG),
        error_messages={"required":CategoryMessage.ICON_REQ_MSG})
    is_icon_svg = fields.Boolean(truthy={1, "1", "True", "true", True}, 
        falsy={0, "0", "False", "false", False}, 
        required=True,
        error_messages={"required":CategoryMessage.IS_ICON_SVG_REQ_MSG, "invalid":CategoryMessage.IS_ICON_SVG_FORMAT_MSG})

class CategoryGetSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    icon = fields.String()
    is_icon_svg = fields.Boolean()