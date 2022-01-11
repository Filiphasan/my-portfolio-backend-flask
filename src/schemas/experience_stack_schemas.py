from marshmallow import Schema, fields
from src.schemas.tech_stack_schema import TechStachGetSchemaForExpStack

class ExperienceStackAddSchema(Schema):
    tech_stack_id = fields.Integer(required=True, error_messages={"required":"Tech Stack Id is required!"})

class ExperienceStackGetSchema(Schema):
    tech_stack = fields.Nested(TechStachGetSchemaForExpStack)