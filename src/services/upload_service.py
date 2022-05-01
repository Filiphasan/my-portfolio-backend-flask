from datetime import datetime
import os
from db import db

from src.models.upload import UploadModel
from src.services import ServiceMessage
from src.utils.response import success_upload_response, error_response

upload_path = os.environ.get("UPLOAD_PATH", "static/uploads")

def upload_file(file):
    try:
        if file:
            now = datetime.now().timestamp()
            filename = file.filename.split(".")[0] + str(now) + "." + file.filename.split(".")[1]
            file_path = upload_path + "/" + filename
            file.save(file_path)
            new_upload = UploadModel(
                file_path= file_path,
                filename= filename,
                upload_for="",
                upload_for_id=""
            )
            db.session.add(new_upload)
            db.session.commit()
            return success_upload_response(file_path, upload_path, ServiceMessage.UPLOAD_SUCCESS, 200)
        else:
            return error_response(ServiceMessage.NOT_FOUND, 404)
    except Exception as error:
        return error_response(str(error), 500)