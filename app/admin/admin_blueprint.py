from flask import Blueprint , jsonify , request, make_response
from app.admin.admin_module import admin_module
from app.auth import auth_check, level_define

admin_handler = Blueprint('admin_handler', __name__)

@admin_handler.route('/admin_allissues' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_all_issues_route(userid = -1):
    msg = admin_module.get_all_issues()
    return jsonify(msg)

@admin_handler.route('/admin_updateissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_update_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.update_issue(request_json)
    return jsonify(msg)

@admin_handler.route('/admin_delissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_delete_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.delete_issue(request_json)
    return jsonify(msg)

@admin_handler.route('/admin_queryissue' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_issue_route(userid = -1):
    request_json = request.json
    msg = admin_module.get_issue_content(request_json)
    return jsonify(msg)

@admin_handler.route('/admin_all_suggestions' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_all_suggestion_route(userid = -1):
    msg = admin_module.get_all_suggestions()
    return jsonify(msg)

@admin_handler.route('/admin_query_suggestion' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_suggestion_route(userid = -1):
    request_json = request.json
    msg = admin_module.get_suggestion_content(request_json)
    return jsonify(msg)

@admin_handler.route('/admin_getstaffs' , methods=['GET'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_get_staffs_route(userid = -1):
    msg = admin_module.get_staffs()
    return jsonify(msg)

@admin_handler.route('/admin_addstaff' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_add_staff_route(userid = -1):
    request_json = request.json
    msg = admin_module.add_staff(request_json)
    return jsonify(msg)

@admin_handler.route('/admin_delstaff' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def admin_del_staff_route(userid = -1):
    request_json = request.json
    msg = admin_module.del_staff(request_json)
    return jsonify(msg)