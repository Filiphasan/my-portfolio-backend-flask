from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.experience_schema import ExperienceAddEditSchema
from src.services.experience_service import list_experience, list_experience_non_delete, get_experience, add_experience, edit_experience, soft_delete_experience
from src.utils.decorator import role_required
from src.utils.role_enum import Roles
from src.controllers import authorizations

experience_ns = Namespace("experience", "Experience CRUD Operations", authorizations=authorizations)

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
    @experience_ns.doc("Get Experience List", security="JWTTokenAuth")
    @experience_ns.response(200, "Success", [experience_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_experience()
    
    @experience_ns.doc("Add Experience", security="JWTTokenAuth")
    @experience_ns.response(200, "Success", experience_get_model)
    @experience_ns.expect(experience_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def post(self):
        req_json = request.get_json()
        data = experience_add_edit_schema.load(req_json)
        return add_experience(data)

@experience_ns.route("/public")
class ExperiencePublicResource(Resource):
    @experience_ns.doc("Get Experience List")
    @experience_ns.response(200, "Success", [experience_get_model])
    def get(self):
        return list_experience_non_delete()

@experience_ns.route("/<id>")
@experience_ns.param("id", "Experience Identity Number")
class ExperienceResource(Resource):
    @experience_ns.doc("Get Experience", security="JWTTokenAuth")
    @experience_ns.response(200, "Success", experience_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_experience(id)
    
    @experience_ns.doc("Edit Experience", security="JWTTokenAuth")
    @experience_ns.response(200, "Success", experience_get_model)
    @experience_ns.expect(experience_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def put(self, id):
        req_json = request.get_json()
        data = experience_add_edit_schema.load(req_json)
        return edit_experience(id, data)
    
    @experience_ns.doc("Delete Experience", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value])
    def delete(self, id):
        return soft_delete_experience(id)
    
