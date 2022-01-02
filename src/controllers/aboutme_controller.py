from flask_restx import Namespace, fields, Resource
from flask import request

from src.services.aboutme_service import list_aboutme, get_about_me, edit_about_me
from src.schemas.aboutme_schema import AboutMeSchema

aboutme_ns = Namespace('aboutme', "About Me Operations")

aboutme_get_model = aboutme_ns.model("AboutMe Get",{
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

aboutme_update_model = aboutme_ns.model("AboutMe Update",{
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

@aboutme_ns.route("/")
class AboutMeListResource(Resource):
    @aboutme_ns.doc("Get About Me List")
    @aboutme_ns.response(200, "Get List Success", [aboutme_get_model])
    def get(self):
        return list_aboutme()

@aboutme_ns.route("/<id>")
@aboutme_ns.param("id","About Me Id Field (UUID)")
class AboutMeResource(Resource):
    @aboutme_ns.doc("Get About Me")
    @aboutme_ns.response(200, "Get Success", aboutme_get_model)
    def get(self, id):
        return get_about_me(id)
    
    @aboutme_ns.doc("Update About Me")
    @aboutme_ns.expect(aboutme_update_model)
    @aboutme_ns.response(200, "Update Success", aboutme_get_model)
    def put(self, id):
        req_json = request.get_json()
        data = aboutme_update_schema.load(req_json)
        return edit_about_me(id, data)