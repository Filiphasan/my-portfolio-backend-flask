from marshmallow import Schema, fields, validate
from src.schemas.messages.experience import ExperienceMessage
from src.schemas.experience_stack_schemas import ExperienceStackGetSchema

class ExperienceAddEditSchema(Schema):
    title = fields.String(required=True,
        validate=validate.Length(10, 100, error=ExperienceMessage.TITLE_LEN_MSG),
        error_messages={"required":ExperienceMessage.TITLE_REQ_MSG})
    company = fields.String(required=True,
        validate=validate.Length(5, 100, error=ExperienceMessage.COMPANY_LEN_MSG),
        error_messages={"required":ExperienceMessage.COMPANY_REQ_MSG})
    start_date = fields.Date(format="%Y-%m-%d", required=True,
        error_messages={"required":ExperienceMessage.START_DATE_REQ_MSG, "invalid":ExperienceMessage.START_DATE_FORMAT_MSG})
    end_date = fields.Date(format="%Y-%m-%d", required=True,
        error_messages={"required":ExperienceMessage.END_DATE_REQ_MSG, "invalid":ExperienceMessage.END_DATE_FORMAT_MSG})
    description = fields.String(required=True,
        validate=validate.Length(30, 300, error=ExperienceMessage.DESC_LEN_MSG),
        error_messages={"required":ExperienceMessage.DESC_REQ_MSG})
    experience_stacks = fields.List(fields.Integer(), required=True,
        validate=validate.Length(min=1, error=ExperienceMessage.STACKS_LEN_MSG),
        error_messages={"required":ExperienceMessage.STACKS_REQ_MSG})

class ExperienceGetSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    company = fields.String()
    start_date = fields.Date(format="%Y-%m-%d")
    end_date = fields.Date(format="%Y-%m-%d")
    description = fields.String()
    experience_stacks = fields.List(fields.Nested(ExperienceStackGetSchema))