from datetime import datetime
from db import db

from src.schemas.article_schema import ArticleGetListSchema, ArticleGetSchema
from src.utils.response import success_response, success_data_response, error_response
from src.services import ServiceMessage
from src.models.article import ArticleModel
from src.models.article_tag import ArticleTagModel
from src.models.comment import CommentModel

article_schema = ArticleGetSchema()
article_schema_for_add_edit = ArticleGetListSchema()
article_list_schema = ArticleGetListSchema(many=True)

def list_article():
    try:
        articles = ArticleModel.query.all()
        if articles:
            data = article_list_schema.dump(articles)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def list_article_non_delete():
    try:
        articles = ArticleModel.query.filter_by(is_deleted=False).all()
        if articles:
            data = article_list_schema.dump(articles)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def list_article_by_category(category_id):
    try:
        articles = ArticleModel.query.filter_by(category_id=category_id).all()
        if articles:
            data = article_list_schema.dump(articles)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def list_article_by_tag(tag_id):
    try:
        articles = ArticleModel.query.filter(ArticleModel.tags.any(tag_id=tag_id)).all()
        if articles:
            data = article_list_schema.dump(articles)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(str(error), 500)

def get_article(id):
    try:
        article = ArticleModel.query.filter_by(id=id).first()
        print(article)
        if article:
            data = article_schema.dump(article)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_article(data):
    try:
        new_article = ArticleModel(
            title= data["title"],
            thumbnail= data["thumbnail"],
            short_content= data["short_content"],
            content= data["content"],
            category_id= data["category_id"],
            seo_tags="",
            seo_description=""
        )
        for tag in data["tags"]:
            new_article.tags.append(ArticleTagModel(article_id=new_article.id, tag_id=tag))
        db.session.add(new_article)
        db.session.commit()
        db.session.refresh(new_article)
        return_data = article_schema_for_add_edit.dump(new_article)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_article(id, data):
    try:
        article = ArticleModel.query.get(id)
        if article:
            article.title = data["title"]
            article.thumbnail = data["thumbnail"]
            article.short_content = data["short_content"]
            article.content = data["content"]
            article.category_id = data["category_id"]
            article.updated_at = datetime.now()
            for tag in article.tags:
                db.session.delete(tag)
            for tag in data["tags"]:
                article.tags.append(ArticleTagModel(article_id=article.id, tag_id=tag))
            db.session.commit()
            db.session.refresh(article)
            return_data = article_schema_for_add_edit.dump(article)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_article(id):
    try:
        article = ArticleModel.query.get(id)
        if article:
            article.is_deleted = True
            article.updated_at = datetime.now()
            for tag in article.tags:
                db.session.delete(tag)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_article(id):
    try:
        article = ArticleModel.query.join(CommentModel).get(id)
        if article:
            for tag in article.tags:
                db.session.delete(tag)
            for comment in article.comments:
                db.session.delete(comment)
            db.session.delete(article)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)