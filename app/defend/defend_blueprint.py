from flask import Blueprint , jsonify , request, make_response
from app.defend.defend_module import defend_module
from app.auth import auth_check

defend_handler = Blueprint('defend_handler', __name__)

@defend_handler.route('/newissue' , methods=['POST'])
@auth_check()
def defend_issue_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = defend_module.create_issue(request_json)
    return jsonify(msg)

@defend_handler.route('/queryissue' , methods=['POST'])
@auth_check()
def defend_query_route(userid = -1):
    request_json = request.json
    msg = defend_module.query_issue(request_json)
    return jsonify(msg)

@defend_handler.route('/userissues' , methods=['GET'])
@auth_check()
def defend_user_issues_route(userid = -1):
    msg = defend_module.query_user_issues(userid)
    return jsonify(msg)

@defend_handler.route('/delissue' , methods=['POST'])
@auth_check()
def defend_del_issue_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = defend_module.del_issue(request_json)
    return jsonify(msg)