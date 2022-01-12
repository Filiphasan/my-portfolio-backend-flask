from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.category_schema import CategoryAddEditSchema
from src.services.category_service import list_category, get_category, add_category, edit_category, soft_delete_category

category_add_edit_schema = CategoryAddEditSchema()

category_ns = Namespace("category", "Category CRUD Operations")

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

@category_ns.route("/")
class CategoriesResource(Resource):
    @category_ns.doc("Get Category List")
    @category_ns.response(200, "Success", [category_get_model])
    def get(self):
        return list_category()
    
    @category_ns.doc("Add Category")
    @category_ns.response(201, "Success", category_get_model)
    @category_ns.expect(category_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = category_add_edit_schema.load(req_json)
        return add_category(data)

@category_ns.route("/<id>")
@category_ns.param("id", "Category Identity Number")
class CategoryResource(Resource):
    @category_ns.doc("Get Category")
    @category_ns.response(200, "Success", category_get_model)
    def get(self, id):
        return get_category(id)
    
    @category_ns.doc("Edit Category")
    @category_ns.response(200, "Success", category_get_model)
    @category_ns.expect(category_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = category_add_edit_schema.load(req_json)
        return edit_category(id, data)
    
    @category_ns.doc("Delete Category")
    def delete(self, id):
        return soft_delete_category(id)