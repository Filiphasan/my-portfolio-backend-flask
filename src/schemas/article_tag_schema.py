from marshmallow import Schema, fields
from src.schemas.tag_schema import TagGetSchema, TagGetSchemaForArticleList

class ArticleTagGetSchema(Schema):
    tag = fields.Nested(TagGetSchema)