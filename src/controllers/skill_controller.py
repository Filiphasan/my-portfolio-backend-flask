from flask_restx import Resource, fields, Namespace
from flask import request

from src.services.skill_service import add_skill, update_skill, soft_delete, get_skill, list_skills, list_skill_non_delete
from src.schemas.skill_schema import SkillAddEditSchema
from src.utils.decorator import role_required
from src.utils.role_enum import Roles
from src.controllers import authorizations

skill_add_edit_schema = SkillAddEditSchema()

skill_ns = Namespace("skill", "Skill Operations", authorizations=authorizations)

skill_get_model = skill_ns.model("SkillGetModel", {
    "id": fields.String(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_svg": fields.Boolean()
})

skill_add_edit_model = skill_ns.model("SkillAddOrEditModel", {
    "name": fields.String(required=True),
    "icon": fields.String(required=True),
    "is_icon_svg": fields.Boolean(required=True)
})

@skill_ns.route("")
class SkillsResource(Resource):
    @skill_ns.doc("Get Skill List", security="JWTTokenAuth")
    @skill_ns.response(200, "Success", [skill_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_skills()
    
    @skill_ns.doc("Add New Skill", security="JWTTokenAuth")
    @skill_ns.expect(skill_add_edit_model)
    @skill_ns.response(201, "Success", skill_get_model)
    @role_required(roles=[Roles.admin.value])
    def post(self):
        req_json = request.get_json()
        data = skill_add_edit_schema.load(req_json)
        return add_skill(data)

@skill_ns.route("/public")
class SkillPublicResource(Resource):
    @skill_ns.doc("Get Skill List")
    @skill_ns.response(200, "Success", [skill_get_model])
    def get(self):
        return list_skill_non_delete()

@skill_ns.route("/<id>")
@skill_ns.param("id", "Skill Identity Number")
class SkillResource(Resource):
    @skill_ns.doc("Get Skill", security="JWTTokenAuth")
    @skill_ns.response(200, "Success", skill_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_skill(id)
    
    @skill_ns.doc("Update Skill", security="JWTTokenAuth")
    @skill_ns.expect(skill_add_edit_model)
    @skill_ns.response(200, "Success", skill_get_model)
    @role_required(roles=[Roles.admin.value])
    def put(self, id):
        req_json = request.get_json()
        data = skill_add_edit_schema.load(req_json)
        return update_skill(id, data)
    
    @skill_ns.doc("Delete Skill", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value])
    def delete(self, id):
        return soft_delete(id)

