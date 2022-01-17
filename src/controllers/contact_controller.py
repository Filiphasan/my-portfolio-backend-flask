from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.contact_schema import ContactAddSchema
from src.services.contact_service import list_contact, get_contact, add_contact, delete_contact
from src.utils.decorator import role_required
from src.utils.role_enum import Roles
from src.controllers import authorizations

contact_add_schema = ContactAddSchema()

contact_ns = Namespace("contact", "Contact CRUD Operations", authorizations=authorizations)

contact_get_model = contact_ns.model("ContactGetModel", {
    "id": fields.Integer(),
    "first_name": fields.String(),
    "last_name": fields.String(),
    "mail": fields.String(),
    "subject": fields.String(),
    "message": fields.String()
})
contact_add_model = contact_ns.model("ContactAddModel", {
    "first_name": fields.String(),
    "last_name": fields.String(),
    "mail": fields.String(),
    "subject": fields.String(),
    "message": fields.String()
})

@contact_ns.route("")
class ContactsResource(Resource):
    @contact_ns.doc("Get Contact List", security="JWTTokenAuth")
    @contact_ns.response(200, "Success", [contact_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_contact()
    
    @contact_ns.doc("Add Contact List")
    @contact_ns.expect(contact_add_model)
    def post(self):
        req_json = request.get_json()
        data = contact_add_schema.load(req_json)
        return add_contact(data)

@contact_ns.route("/<id>")
@contact_ns.param("id", "Contact Identity Number")
class ContactResource(Resource):
    @contact_ns.doc("Get Contact", security="JWTTokenAuth")
    @contact_ns.response(200, "Success", contact_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_contact(id)
    
    @contact_ns.doc("Delete Contact", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value])
    def delete(self, id):
        return delete_contact(id)