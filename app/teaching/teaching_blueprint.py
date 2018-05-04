from flask import Blueprint , jsonify , request, make_response
from app.teaching.teaching_module import teaching_module
from app.auth import auth_check

teaching_handler = Blueprint('teaching_handler', __name__)

@teaching_handler.route('/newclass' , methods=['POST'])
@auth_check()
def teaching_class_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = teaching_module.create_class(request_json)
    return jsonify(msg)

@teaching_handler.route('/queryclass' , methods=['POST'])
def teaching_query_route():
    request_json = request.json
    msg = teaching_module.query_class(request_json)
    return jsonify(msg)

@teaching_handler.route('/userclasses' , methods=['GET'])
@auth_check()
def teaching_user_classes_route(userid = -1):
    msg = teaching_module.query_user_classes(userid)
    return jsonify(msg)

@teaching_handler.route('/delclass' , methods=['POST'])
def teaching_del_class_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = teaching_module.del_class(request_json)
    return jsonify(msg)