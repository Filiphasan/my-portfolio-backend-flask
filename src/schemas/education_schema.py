from marshmallow import Schema, fields, validate
from src.schemas.messages.education import EducationMessages

class EducationAddEditSchema(Schema):
    institution = fields.String(required=True,
        validate=validate.Length(10, 100, error=EducationMessages.INSTITUTION_LEN_MSG),
        error_messages={"required":EducationMessages.INSTITUTION_REQ_MSG})
    title = fields.String(required=True,
        validate=validate.Length(10, 100, error=EducationMessages.TITLE_LEN_MSG),
        error_messages={"required":EducationMessages.TITLE_REQ_MSG})
    begin_date = fields.Date(format="%Y-%m-%d", required=True,
        error_messages={"required":EducationMessages.BEGIN_DATE_REQ_MSG,"format":EducationMessages.BEGIN_DATE_FORMAT_MSG})
    end_date = fields.Date(format="%Y-%m-%d", required=True,
        error_messages={"required":EducationMessages.END_DATE_REQ_MSG,"format":EducationMessages.END_DATE_FORMAT_MSG})
    avarage = fields.String(required=True,
        validate=validate.Length(3, 20, error=EducationMessages.AVARAGE_LEN_MSG),
        error_messages={"required":EducationMessages.AVARAGE_REQ_MSG})
    description = fields.String(required=True,
        validate=validate.Length(40, 400, error=EducationMessages.DESC_LEN_MSG),
        error_messages={"required":EducationMessages.DESC_REQ_MSG})

class EducationGetSchema(Schema):
    id = fields.Integer()
    institution = fields.String()
    title = fields.String()
    begin_date = fields.Date(format="%Y-%m-%d")
    end_date = fields.Date(format="%Y-%m-%d")
    avarage = fields.String()
    description = fields.String()
