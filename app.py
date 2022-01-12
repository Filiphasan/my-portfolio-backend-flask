from flask import Flask, Blueprint, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from flask_restx import Api

from db import db
from ma import ma
import os

from src.utils.data_seed import seed_data
from src.controllers.user_controller import UserResource, UserListResource, user_ns
from src.controllers.auth_controller import AuthResource, auth_ns
from src.controllers.aboutme_controller import AboutMeListResource, AboutMeResource, aboutme_ns
from src.controllers.skill_controller import SkillResource, SkillsResource, skill_ns
from src.controllers.education_controller import EducationsResource, EducationResource, education_ns
from src.controllers.tech_stack_controller import TechStackResource, TechsResource, tech_ns
from src.controllers.experience_controller import ExperiencesResource, ExperienceResource, experience_ns
from src.controllers.interest_controller import InterestsResource, InterestResource, interest_ns
from src.controllers.contact_controller import ContactsResource, ContactResource, contact_ns
from src.controllers.category_controller import CategoriesResource, CategoryResource, category_ns

#Import db table classes because alembic doesn't detected table models. User doesn't need import because user resource import user service and user service import user model.
from src.models.comment import CommentModel
from src.models.article import ArticleModel
from src.models.article_tag import ArticleTagModel
from src.models.tag import TagModel
from src.models.project import ProjectModel
from src.models.project_stack import ProjectStackModel

app = Flask(__name__)

@app.route("/")
def server():
    return "Server is Working!"

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, doc='/doc', title='Flask Rest Structure')
app.register_blueprint(blueprint)

load_dotenv(".env")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ.get("SECRET_KEY", 'application_secret_key') #Example: c094b11d-8eb1-450b-949a-f83d9564c923
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db, compare_type=True) #compare_type=True, if change column property(length) alembic not detect, s

# Implement Namespace In Api right below
api.add_namespace(user_ns)
api.add_namespace(auth_ns)
api.add_namespace(aboutme_ns)
api.add_namespace(skill_ns)
api.add_namespace(education_ns)
api.add_namespace(tech_ns)
api.add_namespace(experience_ns)
api.add_namespace(interest_ns)
api.add_namespace(contact_ns)
api.add_namespace(category_ns)

#Implement Resource In NameSpace right below
user_ns.add_resource(UserResource, '/<id>')
user_ns.add_resource(UserListResource, '/')
auth_ns.add_resource(AuthResource, '/')
aboutme_ns.add_resource(AboutMeListResource, '/')
aboutme_ns.add_resource(AboutMeResource, '/<id>')
skill_ns.add_resource(SkillResource, '/<id>')
skill_ns.add_resource(SkillsResource, '/')
education_ns.add_resource(EducationsResource, '/')
education_ns.add_resource(EducationResource, '/<id>')
tech_ns.add_resource(TechsResource, '/')
tech_ns.add_resource(TechStackResource, '/<id>')
experience_ns.add_resource(ExperiencesResource, '/')
experience_ns.add_resource(ExperienceResource, '/<id>')
interest_ns.add_resource(InterestsResource, '/')
interest_ns.add_resource(InterestResource, '/<id>')
contact_ns.add_resource(ContactsResource, '/')
contact_ns.add_resource(ContactResource, '/<id>')
category_ns.add_resource(CategoriesResource, '/')
category_ns.add_resource(CategoryResource, '/<id>')

@app.before_first_request
def create_table():
    # If you use flask migrate with alembic, don't need this method. We create and edit table with flask-migrate.
    # db.create_all()
    seed_data() #This is data seed method.

# If Marshmallow load data not successful, Marshmallow return ValidationError and error descriptions.
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

# Global Error Handling
@app.errorhandler(Exception)
def handler_global_error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    # return jsonify({"status":"error","message":"Ooops! Something went wrong!"}), code #This is for production.
    return jsonify({"status":"error","message":str(error)}), code

if __name__ == "__main__":
    # db.init_app(app)
    # ma.init_app(app)
    app.run(port=5000, debug=True)