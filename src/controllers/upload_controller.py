from flask_restx import Resource, Namespace
from flask import request

from src.services.upload_service import upload_file
from src.controllers import authorizations
from src.utils.decorator import role_required
from src.utils.role_enum import Roles

upload_ns = Namespace("upload", "Upload File Operations", authorizations=authorizations)

@upload_ns.route("")
class UploadsResource(Resource):
    @upload_ns.doc("Upload File", security="JWTTokenAuth")
    @role_required(roles=[Roles.admin.value, Roles.admin.author.value])
    def post(self):
        file = request.files.get("file")
        return upload_file(file)