from marshmallow import Schema, fields, validate
from src.schemas.messages.project import ProjectMessage

class ProjectAddEditSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=10, max=80, error=ProjectMessage.NAME_LEN_MSG),
        error_messages={"required":ProjectMessage.NAME_REQ_MSG}
    )
    description = fields.String(
        required=True,
        validate=validate.Length(30, 300, error=ProjectMessage.DESC_LEN_MSG),
        error_messages={"required":ProjectMessage.DESC_REQ_MSG}
    )
    release_date = fields.Date(
        format="%Y-%m-%d",
        required=True,
        error_messages={"required":ProjectMessage.RD_REQ_MSG,"invalid":ProjectMessage.RD_FORMAT_MSG}
    )
    has_repo = fields.Boolean(
        truthy={1, "1", "True", "true", True}, 
        falsy={0, "0", "False", "false", False}, 
        required=True,
        error_messages={"required":ProjectMessage.HAS_REPO_REQ_MSG,"invalid":ProjectMessage.HAS_REPO_INVALID_MSG}
    )
    repo_url = fields.String(
        required=True,
        validate=validate.Length(20,240,error=ProjectMessage.REPO_URL_LEN_MSG),
        error_messages={"required":ProjectMessage.REPO_URL_REQ_MSG}
    )
    has_demo = fields.Boolean(
        truthy={1, "1", "True", "true", True}, 
        falsy={0, "0", "False", "false", False}, 
        required=True,
        error_messages={"required":ProjectMessage.HAS_DEMO_REQ_MSG,"invalid":ProjectMessage.HAS_DEMO_INVALID_MSG}
    )
    demo_url = fields.String(
        required=True,
        validate=validate.Length(20,240,error=ProjectMessage.DEMO_URL_LEN_MSG),
        error_messages={"required":ProjectMessage.DEMO_URL_REQ_MSG}
    )
    project_stacks = fields.List(
        fields.Integer(),
        required=True,
        validate=validate.Length(min=1, error=ProjectMessage.STACKS_LEN_MSG),
        error_messages={"required":ProjectMessage.STACKS_REQ_MSG}
    )