from flask import Blueprint , jsonify , request, make_response
from app.admin.admin_module import admin_module
from app.auth import auth_check, level_define

admin_handler = Blueprint('admin_handler', __name__)

@admin_handler.route('/issues' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_all_issues_route(userid = -1):
    msg = admin_module.get_all_issues()
    return jsonify(msg)

@admin_handler.route('/updateissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_update_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.update_issue(request_json)
    return jsonify(msg)

@admin_handler.route('/delissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_delete_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.delete_issue(request_json)
    return jsonify(msg)

@admin_handler.route('/queryissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.get_issue_content(request_json)
    return jsonify(msg)

@admin_handler.route('/suggestions' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_all_suggestion_route(userid = -1):
    msg = admin_module.get_all_suggestions()
    return jsonify(msg)

@admin_handler.route('/querysuggestion' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_suggestion_route(userid = -1):
    request_json = request.json
    msg = admin_module.get_suggestion_content(request_json)
    return jsonify(msg)

@admin_handler.route('/getstaffs' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_staffs_route(userid = -1):
    msg = admin_module.get_staffs()
    return jsonify(msg)

@admin_handler.route('/addstaff' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_add_staff_route(userid = -1):
    request_json = request.json
    msg = admin_module.add_staff(request_json)
    return jsonify(msg)

@admin_handler.route('/delstaff' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_del_staff_route(userid = -1):
    request_json = request.json
    msg = admin_module.del_staff(request_json)
    return jsonify(msg)

@admin_handler.route('/queryuser' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_query_userinfo_route(userid = -1):
    request_json = request.json
    msg = admin_module.get_user_info(request_json)
    return jsonify(msg)