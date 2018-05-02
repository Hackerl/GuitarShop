from flask import Blueprint , jsonify , request, make_response
from app.user.user_module import user_module
from app.auth import auth_check
from datetime import datetime, timedelta

user_handler = Blueprint('user_handler', __name__)

@user_handler.route('/login' , methods=['POST'])
def user_login_route():
    request_json = request.json
    success, msg, token = user_module.login(request_json)
    if success:
        response=make_response(jsonify(msg))
        outdate = datetime.today() + timedelta(days=10)
        response.set_cookie('token',token, expires = outdate)
        return response
    else:
        return jsonify(msg)

@user_handler.route('/register' , methods=['POST'])
def user_register_route():
    request_json = request.json
    msg = user_module.register(request_json)
    return jsonify(msg)

@user_handler.route('/userinfo' , methods=['GET'])
@auth_check()
def user_info_route(userid = -1):
    msg = user_module.getinfo(userid)
    return jsonify(msg)

@user_handler.route('/resetpwd' , methods=['POST'])
@auth_check()
def user_resetpwd_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = user_module.reset_password(request_json)
    return jsonify(msg)

@user_handler.route('/setinfo' , methods=['POST'])
@auth_check()
def user_set_info_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = user_module.set_user_info(request_json)
    return jsonify(msg)

@user_handler.route('/setserverinfo' , methods=['POST'])
@auth_check()
def user_set_serverinfo_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = user_module.set_server_info(request_json)
    return jsonify(msg)

@user_handler.route('/sethead' , methods=['POST'])
@auth_check()
def user_set_head_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = user_module.set_user_head(request_json)
    return jsonify(msg)