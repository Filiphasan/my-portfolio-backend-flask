from marshmallow import Schema, fields, validate
from src.schemas.category_schema import CategoryGetSchema
from src.schemas.comment_schema import CommentGetSchema
from src.schemas.article_tag_schema import ArticleTagGetSchema
from src.schemas.messages.article import ArticleMessage

class ArticleAddEditSchema(Schema):
    title = fields.String(
        required=True,
        validate=validate.Length(10,120,error=ArticleMessage.TITLE_LEN_MSG),
        error_messages={"required":ArticleMessage.TITLE_REQ_MSG}
    )
    thumbnail = fields.String(
        required=True,
        validate=validate.Length(max=240, error=ArticleMessage.THUMBNAIL_LEN_MSG),
        error_messages={"required":ArticleMessage.THUMBNAIL_REQ_MSG}
    )
    short_content = fields.String(
        required=True,
        validate=validate.Length(100, 400, error=ArticleMessage.SH_CONTENT_LEN_MSG),
        error_messages={"required":ArticleMessage.SH_CONTENT_REQ_MSG}
    )
    content = fields.String(
        required=True,
        validate=validate.Length(min=10, error=ArticleMessage.CONTENT_LEN_MSG),
        error_messages={"required":ArticleMessage.CONTENT_REQ_MSG}
    )
    category_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1,error=ArticleMessage.CATEGORY_ID_RANGE_MSG),
        error_messages={"required":ArticleMessage.CATEGORY_ID_REQ_MSG}
    )
    tags = fields.List(
        fields.Integer(
            validate=validate.Range(min=1,error=ArticleMessage.TAG_ID_RANGE_MSG)
        ),
        required=True,
        validate=validate.Length(min=1, error=ArticleMessage.TAGS_LEN_MSG),
        error_messages={"required":ArticleMessage.TAGS_REQ_MSG}
    )

class ArticleGetListSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    thumbnail = fields.String()
    short_content = fields.String()
    category = fields.Nested(CategoryGetSchema)
    views_count = fields.Integer()
    comment_count = fields.Integer()
    tags = fields.List(fields.Nested(ArticleTagGetSchema))

class ArticleGetSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    thumbnail = fields.String()
    short_content = fields.String()
    content = fields.String()
    category_id = fields.Integer()
    category = fields.Nested(CategoryGetSchema)
    views_count = fields.Integer()
    comment_count = fields.Integer()
    comments = fields.List(fields.Nested(CommentGetSchema))
    tags = fields.List(fields.Nested(ArticleTagGetSchema))