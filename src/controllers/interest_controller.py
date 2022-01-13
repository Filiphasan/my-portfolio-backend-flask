from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.interest_schema import InterestAddEditSchema
from src.services.interest_service import list_interest, get_interest, add_interest, edit_interest, soft_delete_interest

interest_ns = Namespace("interest", "Interests CRUD Operations")

interest_add_edit_schema = InterestAddEditSchema()

interest_get_model = interest_ns.model("InterestGetModel", {
    "id": fields.String(),
    "title": fields.String()
})
interest_add_edit_model = interest_ns.model("InterestAddEditModel", {
    "title": fields.String()
})

@interest_ns.route("/")
class InterestsResource(Resource):
    @interest_ns.doc("Get Interest List")
    @interest_ns.response(200, "Success", [interest_get_model])
    def get(self):
        return list_interest()
    
    @interest_ns.doc("Add Interest")
    @interest_ns.response(201, "Success", interest_get_model)
    @interest_ns.expect(interest_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = interest_add_edit_schema.load(req_json)
        return add_interest(data)
    
@interest_ns.route("/<id>")
@interest_ns.param("id", "Interest Identity Number")
class InterestResource(Resource):
    @interest_ns.doc("Get Interest")
    @interest_ns.response(200, "Success", interest_get_model)
    def get(self, id):
        return get_interest(id)
    
    @interest_ns.doc("Edit Interest")
    @interest_ns.response(200, "Success", interest_get_model)
    @interest_ns.expect(interest_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = interest_add_edit_schema.load(req_json)
        return edit_interest(id, data)
    
    @interest_ns.doc("Delete Interest")
    def delete(self, id):
        return soft_delete_interest(id)