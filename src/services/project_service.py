from datetime import datetime
from db import db

from src.models.project import ProjectModel
from src.models.project_stack import ProjectStackModel
from src.schemas.project_schema import ProjectGetSchema
from src.services import ServiceMessage
from src.utils.response import success_response, success_data_response, error_response

project_schema = ProjectGetSchema()
project_list_schema = ProjectGetSchema(many=True)


def list_project():
    try:
        projects = ProjectModel.query.all()
        if projects:
            data = project_list_schema.dump(projects)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def list_project_non_delete():
    try:
        projects = ProjectModel.query.filter_by(is_deleted=False).all()
        if projects:
            data = project_list_schema.dump(projects)
            return success_data_response(data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def add_project(data):
    try:
        new_project = ProjectModel(
            name= data["name"],
            description= data["description"],
            release_date= data["release_date"],
            has_repo= data["has_repo"],
            repo_url= data["repo_url"],
            has_demo= data["has_demo"],
            demo_url= data["demo_url"]
        )
        for stack in data["project_stacks"]:
            new_project.project_stacks.append(ProjectStackModel(project_id=new_project.id, tech_stack_id=stack))
        db.session.add(new_project)
        db.session.commit()
        db.session.refresh(new_project)
        return_data = project_schema.dump(new_project)
        return success_data_response(return_data, 201)
    except Exception as error:
        return error_response(str(error), 500)

def get_project(id):
    try:
        project = ProjectModel.query.filter_by(id=id).first()
        if project:
            return_data = project_schema.dump(project)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def edit_project(id, data):
    try:
        project = ProjectModel.query.filter_by(id=id).first()
        if project:
            project.name = data["name"]
            project.description = data["description"]
            project.release_date = data["release_date"]
            project.has_repo = data["has_repo"]
            project.repo_url = data["repo_url"]
            project.has_demo = data["has_demo"]
            project.demo_url = data["demo_url"]
            project.updated_at = datetime.now()
            for stack in project.project_stacks:
                db.session.delete(stack)
            for stack in data["project_stacks"]:
                project.project_stacks.append(ProjectStackModel(project_id=project.id, tech_stack_id=stack))
            db.session.commit()
            return_data = project_schema.dump(project)
            return success_data_response(return_data, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def soft_delete_project(id):
    try:
        project = ProjectModel.query.filter_by(id=id).first()
        if project and not project.is_deleted:
            for stack in project.project_stacks:
                db.session.delete(stack)
            project.is_deleted = True
            project.updated_at = datetime.now()
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)

def delete_project(id):
    try:
        project = ProjectModel.query.filter_by(id=id).first()
        if project:
            for stack in project.project_stacks:
                db.session.delete(stack)
            db.session.delete(project)
            db.session.commit()
            return success_response(ServiceMessage.DELETE_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(ServiceMessage.SERVER_ERROR, 500)