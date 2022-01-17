from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.project_schema import ProjectAddEditSchema
from src.services.project_service import list_project, list_project_non_delete, add_project, get_project, edit_project, soft_delete_project
from src.utils.decorator import role_required
from src.utils.role_enum import Roles
from src.controllers import authorizations

project_add_edit_schema = ProjectAddEditSchema()

project_ns = Namespace("project", "Project CRUD Operations", authorizations=authorizations)

tech_stack_model = project_ns.model("TechStackModel", {
    "id": fields.Integer(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_devicon": fields.Boolean()
})
project_stack_get_model = project_ns.model("ProjectStackGetModel",{
    "tech_stack": fields.Nested(model=tech_stack_model)
})
project_get_model = project_ns.model("ProjectGetModel",{
    "id": fields.Integer(),
    "name": fields.String(),
    "description": fields.String(),
    "release_date": fields.Date(format="%Y-%m-%d"),
    "has_repo": fields.Boolean(),
    "repo_url": fields.String(),
    "has_demo": fields.Boolean(),
    "demo_url": fields.String(),
    "project_stacks": fields.List(fields.Nested(model=project_stack_get_model))
})
project_add_edit_model = project_ns.model("ProjectAddEdirModel",{
    "name": fields.String(),
    "description": fields.String(),
    "release_date": fields.Date(format="%Y-%m-%d"),
    "has_repo": fields.Boolean(),
    "repo_url": fields.String(),
    "has_demo": fields.Boolean(),
    "demo_url": fields.String(),
    "project_stacks": fields.List(fields.Integer())
})

@project_ns.route("")
class ProjectsResource(Resource):
    @project_ns.doc("Get Project List", security="JWTTokenAuth")
    @project_ns.response(200, "Success", [project_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_project()
    
    @project_ns.doc("Add Project", security="JWTTokenAuth")
    @project_ns.response(201, "Success", project_get_model)
    @project_ns.expect(project_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def post(self):
        req_json = request.get_json()
        data = project_add_edit_schema.load(req_json)
        return add_project(data)

@project_ns.route("/public")
class ProjectsPublicResource(Resource):
    @project_ns.doc("Get Project List")
    @project_ns.response(200, "Success", [project_get_model])
    def get(self):
        return list_project_non_delete()

@project_ns.route("/<id>")
@project_ns.param("id", "Project Identity Number")
class ProjectResource(Resource):
    @project_ns.doc("Get Project", security="JWTTokenAuth")
    @project_ns.response(200, "Success", project_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_project(id)
    
    @project_ns.doc("Edit Project", security="JWTTokenAuth")
    @project_ns.response(200, "Success", project_get_model)
    @project_ns.expect(project_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def put(self, id):
        req_json = request.get_json()
        data = project_add_edit_schema.load(req_json)
        return edit_project(id, data)
    
    @project_ns.doc("Delete Project", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value])
    def delete(self, id):
        return soft_delete_project(id)