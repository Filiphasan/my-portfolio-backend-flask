from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.tech_stack_schema import TechStackAddEditSchema
from src.services.tech_stack_service import list_tech_stack, get_tech_stack, add_tech_stack, edit_tech_stack, soft_delete_tech_stack

tech_stack_add_edit_schema = TechStackAddEditSchema()

tech_ns = Namespace("tech-stack", "Tech Stack Operation")

tech_stack_get_model = tech_ns.model("TechStackGetModel", {
    "id": fields.Integer(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_devicon": fields.Boolean(),
    "created_at": fields.DateTime(dt_format="%Y-%m-%d %H:%M"),
    "updated_at": fields.DateTime(dt_format="%Y-%m-%d %H:%M")
})

tech_stack_add_edit_model = tech_ns.model("TechStackAddEditModel", {
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_devicon": fields.Boolean()
})

@tech_ns.route("/")
class TechsResource(Resource):
    @tech_ns.doc("Get Tech Stack List")
    @tech_ns.response(200, "Success", [tech_stack_get_model])
    def get(self):
        return list_tech_stack()
    
    @tech_ns.doc("Add Tech Stack")
    @tech_ns.response(201, "Success", tech_stack_get_model)
    @tech_ns.expect(tech_stack_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = tech_stack_add_edit_schema.load(req_json)
        return add_tech_stack(data)

@tech_ns.route("/<id>")
@tech_ns.param("id", "Tech Stack Identity Number")
class TechStackResource(Resource):
    @tech_ns.doc("Get Tech Stack")
    @tech_ns.response(200, "Success", tech_stack_get_model)
    def get(self, id):
        return get_tech_stack(id)

    @tech_ns.doc("Update Tech Stack")
    @tech_ns.response(200, "Success", tech_stack_get_model)
    @tech_ns.expect(tech_stack_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = tech_stack_add_edit_schema.load(req_json)
        return edit_tech_stack(id, data)
    
    @tech_ns.doc("Delete Tech Stack")
    def delete(self, id):
        return soft_delete_tech_stack(id)