from flask_restx import Resource, Namespace, fields
from flask import request

from src.services.article_service import list_article, list_article_by_category, list_article_by_tag, get_article, add_article, edit_article, soft_delete_article
from src.schemas.article_schema import ArticleAddEditSchema

article_add_edit_schema = ArticleAddEditSchema()

article_ns = Namespace("article", "Article CRUD Operations")

category_model = article_ns.model("CategoryModelForArticle",{
    "id": fields.Integer(),
    "name": fields.String(),
    "icon": fields.String(),
    "is_icon_svg": fields.Boolean()
})
comment_model = article_ns.model("CommentModelForArticle",{
    "id": fields.Integer(),
    "article_id": fields.Integer(),
    "full_name": fields.String(),
    "mail": fields.String(),
    "comment": fields.String()
})
tag_model = article_ns.model("TagModelForArticle",{
    "tag": fields.String()
})
article_get_list_model = article_ns.model("ArticleGetListModel", {
    "id": fields.Integer(),
    "title": fields.String(),
    "thumbnail": fields.String(),
    "short_content": fields.String(),
    "category":fields.Nested(model=category_model),
    "views_count": fields.Integer(),
    "comment_count": fields.Integer(),
    "tags":fields.List(fields.Nested(model=tag_model))
})
article_get_model = article_ns.model("ArticleGetModel", {
    "id": fields.Integer(),
    "title": fields.String(),
    "thumbnail": fields.String(),
    "short_content": fields.String(),
    "content": fields.String(),
    "category_id": fields.Integer(),
    "category": fields.Nested(model=category_model),
    "views_count": fields.Integer(),
    "comment_count": fields.Integer(),
    "comments": fields.List(fields.Nested(model=comment_model))
})
article_add_edit_model = article_ns.model("ArticleAddEditModel",{
    "title": fields.String(),
    "thumbnail": fields.String(),
    "short_content": fields.String(),
    "content": fields.String(),
    "category_id": fields.Integer(),
    "tags": fields.List(fields.Integer())
})

@article_ns.route("/")
class ArticlesResource(Resource):
    @article_ns.doc("Get Article List")
    @article_ns.response(200, "Success", [article_get_list_model])
    def get(self):
        return list_article()
    
    @article_ns.doc("Add Article")
    @article_ns.response(201, "Success", article_get_model)
    @article_ns.expect(article_add_edit_model)
    def post(self):
        req_json = request.get_json()
        data = article_add_edit_schema.load(req_json)
        return add_article(data)

@article_ns.route("/category/<category_id>")
@article_ns.param("category_id", "Category Identity Number")
class ArticlesCategoryResource(Resource):
    @article_ns.doc("Get Article List By Category Id")
    @article_ns.response(200, "Success", [article_get_list_model])
    def get(self, category_id):
        return list_article_by_category(category_id)

@article_ns.route("/tag/<tag_id>")
@article_ns.param("tag_id", "Article Tag Identity Number")
class ArticlesTagResource(Resource):
    @article_ns.doc("Get Article List By Tag Id")
    @article_ns.response(200, "Success",[article_get_list_model])
    def get(self, tag_id):
        return list_article_by_tag(tag_id)
    
@article_ns.route("/<id>")
@article_ns.param("id", "Article Identity Number")
class ArticleResource(Resource):
    @article_ns.doc("Get Article")
    @article_ns.response(200, "Success", article_get_model)
    def get(self, id):
        return get_article(id)
    
    @article_ns.doc("Edit Article")
    @article_ns.response(200, "Success", article_get_model)
    @article_ns.expect(article_add_edit_model)
    def put(self, id):
        req_json = request.get_json()
        data =article_add_edit_schema.load(req_json)
        return edit_article(id, data)
    
    @article_ns.doc("Delete Article")
    def delete(self, id):
        return soft_delete_article(id)
