from flask import Blueprint , jsonify , request, make_response
from app.suggest.suggest_module import suggest_module
from app.auth import auth_check

suggest_handler = Blueprint('suggest_handler', __name__)

@suggest_handler.route('/newsuggest' , methods=['POST'])
@auth_check()
def suggest_new_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = suggest_module.create_suggest(request_json)
    return jsonify(msg)

@suggest_handler.route('/suggestions' , methods=['GET'])
@auth_check()
def suggest_user_route(userid = -1):
    msg = suggest_module.query_user_suggestions(userid)
    return jsonify(msg)

@suggest_handler.route('/querysuggest' , methods=['GET'])
@auth_check()
def suggest_query_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = suggest_module.query_suggestion(request_json)
    return jsonify(msg)