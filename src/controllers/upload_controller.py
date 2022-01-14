from flask_restx import Resource, Namespace
from flask import request

from src.services.upload_service import upload_file

upload_ns = Namespace("upload", "Upload File Operations")

@upload_ns.route("")
class UploadsResource(Resource):
    @upload_ns.doc("Upload File")
    def post(self):
        file = request.files.get("file")
        return upload_file(file)