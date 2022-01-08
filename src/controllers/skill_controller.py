from flask_restx import Resource, fields, Namespace
from flask import request

from src.services.skill_service import add_skill, update_skill, soft_delete, get_skill, list_skills
from src.schemas.skill_schema import SkillAddEditSchema

skill_add_edit_schema = SkillAddEditSchema()

skill_ns = Namespace("skill", "Skill Operations")

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

@skill_ns.route("/")
class SkillsResource(Resource):
    @skill_ns.doc("Get Skill List")
    @skill_ns.response(200, "Success", [skill_get_model])
    def get(self):
        return list_skills()
    
    @skill_ns.doc("Add New Skill")
    @skill_ns.expect(skill_add_edit_model)
    @skill_ns.response(201, "Success", skill_get_model)
    def post(self):
        req_json = request.get_json()
        data = skill_add_edit_schema.load(req_json)
        return add_skill(data)

@skill_ns.route("/<id>")
@skill_ns.param("id", "Skill Identity Number")
class SkillResource(Resource):
    @skill_ns.doc("Get Skill")
    @skill_ns.response(200, "Success", skill_get_model)
    def get(self, id):
        return get_skill(id)
    
    @skill_ns.doc("Update Skill")
    @skill_ns.expect(skill_add_edit_model)
    @skill_ns.response(200, "Success", skill_get_model)
    def put(self, id):
        req_json = request.get_json()
        data = skill_add_edit_schema.load(req_json)
        return update_skill(id, data)
    
    @skill_ns.doc("Delete Skill")
    def delete(self, id):
        return soft_delete(id)

