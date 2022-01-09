from flask_restx import Resource,Namespace, fields
from flask import request

from src.services.education_service import list_education, get_education, add_education, edit_education, soft_delete_education
from src.schemas.education_schema import EducationAddEditSchema

education_ns = Namespace("education", "Education Operations")

education_add_edit_schema = EducationAddEditSchema()

education_get_model = education_ns.model("EducationGetModel", {
    "id": fields.Integer(),
    "institution": fields.String(),
    "title": fields.String(),
    "begin_date": fields.Date(format="%Y-%m-%d"),
    "end_date": fields.Date(format="%Y-%m-%d"),
    "avarage": fields.String(),
    "description": fields.String()
})

education_add_edit_model = education_ns.model("EducationAddEditModel", {
    "institution": fields.String(),
    "title": fields.String(),
    "begin_date": fields.Date(format="%Y-%m-%d"),
    "end_date": fields.Date(format="%Y-%m-%d"),
    "avarage": fields.String(),
    "description": fields.String()
})

@education_ns.route("/")
class EducationsResource(Resource):
    @education_ns.doc("Get Education List")
    @education_ns.response(200, "Success", [education_get_model])
    def get(self):
        return list_education()
    
    @education_ns.doc("Add New Education")
    @education_ns.response(201, "Success", education_get_model)
    @education_ns.expect(education_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = education_add_edit_schema.load(req_json)
        return add_education(data)
    
@education_ns.route("/<id>")
@education_ns.param("id", "Education Identity Number")
class EducationResource(Resource):
    @education_ns.doc("Get Education List")
    @education_ns.response(200, "Success", [education_get_model])
    def get(self, id):
        return get_education(id)
    
    @education_ns.doc("Edit Education")
    @education_ns.response(200, "Success", education_get_model)
    @education_ns.expect(education_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = education_add_edit_schema.load(req_json)
        return edit_education(id, data)
    
    @education_ns.doc("Delete Education")
    def delete(self, id):
        return soft_delete_education(id)