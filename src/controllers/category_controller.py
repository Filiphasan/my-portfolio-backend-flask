from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.category_schema import CategoryAddEditSchema
from src.services.category_service import list_category, list_category_non_delete, get_category, add_category, edit_category, soft_delete_category
from src.utils.decorator import role_required
from src.utils.role_enum import Roles
from src.controllers import authorizations

category_add_edit_schema = CategoryAddEditSchema()

category_ns = Namespace("category", "Category CRUD Operations", authorizations=authorizations)

category_get_model = category_ns.model("CategoryGetModel",{
    "id": fields.Integer(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_svg": fields.Boolean()
})
category_add_edit_model = category_ns.model("CategoryAddEditModel", {
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_svg": fields.Boolean()
})

@category_ns.route("")
class CategoriesResource(Resource):
    @category_ns.doc("Get Category List", security="JWTTokenAuth")
    @category_ns.response(200, "Success", [category_get_model])
    @role_required(roles=[Roles.admin.value])
    def get(self):
        return list_category()
    
    @category_ns.doc("Add Category", security="JWTTokenAuth")
    @category_ns.response(201, "Success", category_get_model)
    @category_ns.expect(category_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def post(self):
        req_json = request.get_json()
        data = category_add_edit_schema.load(req_json)
        return add_category(data)

@category_ns.route("/public")
class CategoryPublicResource(Resource):
    @category_ns.doc("Get Category List")
    @category_ns.response(200, "Success", [category_get_model])
    def get(self):
        return list_category_non_delete()

@category_ns.route("/<id>")
@category_ns.param("id", "Category Identity Number")
class CategoryResource(Resource):
    @category_ns.doc("Get Category", security="JWTTokenAuth")
    @category_ns.response(200, "Success", category_get_model)
    @role_required(roles=[Roles.admin.value])
    def get(self, id):
        return get_category(id)
    
    @category_ns.doc("Edit Category", security="JWTTokenAuth")
    @category_ns.response(200, "Success", category_get_model)
    @category_ns.expect(category_add_edit_model)
    @role_required(roles=[Roles.admin.value])
    def put(self, id):
        req_json = request.get_json()
        data = category_add_edit_schema.load(req_json)
        return edit_category(id, data)
    
    @category_ns.doc("Delete Category", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value])
    def delete(self, id):
        return soft_delete_category(id)