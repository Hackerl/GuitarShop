from flask import Blueprint , jsonify , request, make_response
from app.wiki.wiki_module import wiki_module
from app.auth import auth_check, level_define

wiki_handler = Blueprint('wiki_handler', __name__)


@wiki_handler.route('/newwiki' , methods=['POST'])
@auth_check(level = level_define['ADMIN_LEVEL'])
def wiki_new_route(userid = -1):
    request_json = request.json
    msg = wiki_module.create_question(request_json)
    return jsonify(msg)

@wiki_handler.route('/allwiki' , methods=['GET'])
def wiki_all_route():
    msg = wiki_module.get_all_questions()
    return jsonify(msg)

@wiki_handler.route('/querywiki' , methods=['POST'])
def wiki_query_route():
    request_json = request.json
    msg = wiki_module.query_question(request_json)
    return jsonify(msg)

@wiki_handler.route('/searchwiki' , methods=['POST'])
def wiki_search_route():
    request_json = request.json
    msg = wiki_module.search_question(request_json)
    return jsonify(msg)

@wiki_handler.route('/delwiki' , methods=['POST'])
def wiki_del_route():
    request_json = request.json
    msg = wiki_module.del_question(request_json)
    return jsonify(msg)