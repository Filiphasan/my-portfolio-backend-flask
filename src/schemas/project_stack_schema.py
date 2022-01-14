from marshmallow import Schema, fields
from src.schemas.tech_stack_schema import TechStachGetSchemaForExpStack

class ProjectStackGetSchema(Schema):
    tech_stack = fields.Nested(TechStachGetSchemaForExpStack)