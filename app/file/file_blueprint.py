from flask import Blueprint , jsonify , request
from app.file.file_module import file_module
from app.auth import auth_check

file_handler = Blueprint('file_handler', __name__)

@file_handler.route('/upload' , methods=['POST'])
@auth_check()
def file_upload_route(userid = -1):
    request_files = request.files
    msg = file_module.upload_file(request_files)
    return jsonify(msg)