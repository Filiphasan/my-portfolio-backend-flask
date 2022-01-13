from marshmallow import Schema, fields

class CommentGetSchema(Schema):
    id = fields.Integer()
    article_id = fields.Integer()
    full_name = fields.String()
    mail = fields.String()
    comment = fields.String()