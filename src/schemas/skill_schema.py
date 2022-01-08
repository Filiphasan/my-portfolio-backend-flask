import re
from marshmallow import Schema, fields, validate
from src.schemas.messages.skill import SkillMessages

class SkillAddEditSchema(Schema):
    name = fields.String(required=True, 
        validate=validate.Length(min=1, max=80, error=SkillMessages.NAME_LEN_MSG),
        error_messages={"required":SkillMessages.NAME_REQ_MSG})
    icon = fields.String(required=True,
        validate=validate.Length(min=5, error=SkillMessages.ICON_LEN_MSG),
        error_messages={"required":SkillMessages.ICON_REQ_MSG})
    is_icon_svg = fields.Boolean(truthy={1, "1", "True", "true", True}, 
        falsy={0, "0", "False", "false", False}, 
        required=True,
        error_messages={"required":SkillMessages.IS_ICON_SVG_REQ_MSG})

class SkillGetSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    icon = fields.String()
    is_icon_svg = fields.Boolean()