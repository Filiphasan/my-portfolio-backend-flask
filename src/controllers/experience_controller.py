from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.experience_schema import ExperienceAddEditSchema
from src.services.experience_service import list_experience, get_experience, add_experience, edit_experience, soft_delete_experience

experience_ns = Namespace("experience", "Experience CRUD Operations")

experience_add_edit_schema = ExperienceAddEditSchema()

tech_stack_model = experience_ns.model("TechStackModel", {
    "id": fields.Integer(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_devicon": fields.Boolean()
})

experience_stack_get_model = experience_ns.model("ExperienceStackGetModel",{
    "tech_stack": fields.Nested(model=tech_stack_model)
})

experience_get_model = experience_ns.model("ExperienceGetModel", {
    "id": fields.Integer(),
    "title": fields.String(),
    "company": fields.String(),
    "start_date": fields.Date(format="%Y-%m-%d"),
    "end_date": fields.Date(format="%Y-%m-%d"),
    "description": fields.String(),
    "experience_stacks": fields.List(fields.Nested(model=experience_stack_get_model))
})

experience_add_edit_model = experience_ns.model("ExperienceAddEditModel", {
    "title": fields.String(),
    "company": fields.String(),
    "start_date": fields.Date(format="%Y-%m-%d"),
    "end_date": fields.Date(format="%Y-%m-%d"),
    "description": fields.String(),
    "experience_stacks": fields.List(fields.Integer())
})


@experience_ns.route("")
class ExperiencesResource(Resource):
    @experience_ns.doc("Get Experience List")
    @experience_ns.response(200, "Success", [experience_get_model])
    def get(self):
        return list_experience()
    
    @experience_ns.doc("Add Experience")
    @experience_ns.response(200, "Success", experience_get_model)
    @experience_ns.expect(experience_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = experience_add_edit_schema.load(req_json)
        return add_experience(data)

@experience_ns.route("/<id>")
@experience_ns.param("id", "Experience Identity Number")
class ExperienceResource(Resource):
    @experience_ns.doc("Get Experience")
    @experience_ns.response(200, "Success", experience_get_model)
    def get(self, id):
        return get_experience(id)
    
    @experience_ns.doc("Edit Experience")
    @experience_ns.response(200, "Success", experience_get_model)
    @experience_ns.expect(experience_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = experience_add_edit_schema.load(req_json)
        return edit_experience(id, data)
    
    @experience_ns.doc("Delete Experience")
    def delete(self, id):
        return soft_delete_experience(id)
    
