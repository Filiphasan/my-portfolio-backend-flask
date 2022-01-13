from marshmallow import Schema, fields, validate
from src.schemas.messages.comment import CommentMessage

class CommentAddEditSchema(Schema):
    article_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1, error=CommentMessage.ART_ID_RANGE_MSG),
        error_messages={"required":CommentMessage.ART_ID_REQ_MSG}
    )
    full_name = fields.String(
        required=True,
        validate=validate.Length(min=5, max=50, error=CommentMessage.F_NAME_LEN_MSG),
        error_messages={"required":CommentMessage.F_NAME_REQ_MSG}
    )
    mail = fields.Email(
        required=True,
        error_messages={"required":CommentMessage.MAIL_REQ_MSG, "invalid":CommentMessage.MAIL_INVLD_MSG}
    )
    comment = fields.String(
        required=True,
        validate=validate.Length(min=30, max=400, error=CommentMessage.COMMNT_LEN_MSG),
        error_messages={"required":CommentMessage.COMMNT_REQ_MSG}
    )

class CommentGetSchema(Schema):
    id = fields.Integer()
    article_id = fields.Integer()
    full_name = fields.String()
    mail = fields.String()
    comment = fields.String()