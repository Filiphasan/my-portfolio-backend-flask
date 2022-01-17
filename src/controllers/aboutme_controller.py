from flask_restx import Namespace, fields, Resource
from flask import request

from src.services.aboutme_service import list_aboutme, list_aboutme_non_delete, get_about_me, edit_about_me
from src.schemas.aboutme_schema import AboutMeSchema
from src.utils.decorator import role_required
from src.utils.role_enum import Roles

aboutme_ns = Namespace('aboutme', "About Me RUD Operations")

aboutme_get_model = aboutme_ns.model("AboutMeGet",{
    "id": fields.String(),
    "full_name": fields.String(),
    "job_title": fields.String(),
    "short_desc": fields.String(),
    "profile_photo": fields.String(),
    "birth_date": fields.String(),
    "phone_number": fields.String(),
    "email": fields.String(),
    "short_adress": fields.String()
})

aboutme_update_model = aboutme_ns.model("AboutMeUpdate",{
    "full_name": fields.String(),
    "job_title": fields.String(),
    "short_desc": fields.String(),
    "profile_photo": fields.Raw(),
    "birth_date": fields.Date(),
    "phone_number": fields.String(),
    "email": fields.String(),
    "short_adress": fields.String()
})

aboutme_update_schema = AboutMeSchema()

@aboutme_ns.route("")
class AboutMeListResource(Resource):
    @aboutme_ns.doc("Get About Me List", security="JWTTokenAuth")
    @aboutme_ns.response(200, "Get List Success", [aboutme_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_aboutme()

@aboutme_ns.route("/public")
class AboutMePublicResource(Resource):
    @aboutme_ns.doc("Get AboutMe Public")
    @aboutme_ns.response(200, "Get List Success", aboutme_get_model)
    def get(self):
        return get_about_me(id=1)

@aboutme_ns.route("/<id>")
@aboutme_ns.param("id","About Me Id Field (UUID)")
class AboutMeResource(Resource):
    @aboutme_ns.doc("Get About Me", security="JWTTokenAuth")
    @aboutme_ns.response(200, "Get Success", aboutme_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_about_me(id)
    
    @aboutme_ns.doc("Update About Me", security="JWTTokenAuth")
    @aboutme_ns.expect(aboutme_update_model)
    @aboutme_ns.response(200, "Update Success", aboutme_get_model)
    @role_required(roles=[Roles.admin.value])
    def put(self, id):
        req_json = request.get_json()
        data = aboutme_update_schema.load(req_json)
        return edit_about_me(id, data)