from marshmallow import Schema, fields, validate

class TagAddEditSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(max=20, error="Tag field must be less or equal than 20 characters!"),
        error_messages={"required":"Tag field is required!"}
    )

class TagGetSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class TagGetSchemaForArticleList(Schema):
    name = fields.String()