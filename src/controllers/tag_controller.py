from flask_restx import Resource, Namespace, fields
from flask import request

from src.schemas.tag_schema import TagAddEditSchema
from src.services.tag_service import list_tag, get_tag, add_tag, edit_tag, soft_delete_tag

tag_add_edit_schema = TagAddEditSchema()

tag_ns = Namespace("tag", "Tag CRUD Operations")

tag_get_model = tag_ns.model("TagGetModel", {
    "id": fields.Integer(),
    "name": fields.String()
})
tag_add_edit_model = tag_ns.model("TagAddEditModel",{
    "name":fields.String()
})

@tag_ns.route("/")
class TagsResource(Resource):
    @tag_ns.doc("Get Tag List")
    @tag_ns.response(200, "Success",[tag_get_model])
    def get(self):
        return list_tag()
    
    @tag_ns.doc("Add Tag")
    @tag_ns.response(201, "Success", tag_get_model)
    @tag_ns.expect(tag_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = tag_add_edit_schema.load(req_json)
        return add_tag(data)

@tag_ns.route("/<id>")
@tag_ns.param("id", "Tag Identity Number")
class TagResource(Resource):
    @tag_ns.doc("Get Tag")
    @tag_ns.response(200, "Success", tag_get_model)
    def get(self, id):
        return get_tag(id)
    
    @tag_ns.doc("Edit Tag")
    @tag_ns.response(200, "Success", tag_get_model)
    @tag_ns.expect(tag_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data = tag_add_edit_schema.load(req_json)
        return edit_tag(id, data)
    
    @tag_ns.doc("Delete Tag")
    def delete(self, id):
        return soft_delete_tag(id)