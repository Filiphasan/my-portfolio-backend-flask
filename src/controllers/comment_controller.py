from flask_restx import Resource, Namespace, fields
from flask import request

from src.services.comment_service import add_comment, delete_comment
from src.schemas.comment_schema import CommentAddEditSchema

comment_add_edit_schema = CommentAddEditSchema()

comment_ns = Namespace("comment", "Comment CD Operations")

comment_add_edit_model = comment_ns.model("CommentAddModel",{
    "article_id": fields.Integer(),
    "full_name": fields.String(),
    "mail": fields.String(),
    "comment": fields.String()
})

@comment_ns.route("")
class CommentsResource(Resource):
    @comment_ns.doc("Add Comment")
    @comment_ns.expect(comment_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = comment_add_edit_schema.load(req_json)
        return add_comment(data)

@comment_ns.route("/<id>")
@comment_ns.param("id", "Comment Identity Number")
class CommentResource(Resource):
    @comment_ns.doc("Delete Comment")
    def delete(self, id):
        return delete_comment(id)