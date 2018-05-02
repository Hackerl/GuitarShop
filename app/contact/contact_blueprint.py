from flask import Blueprint , jsonify , request, make_response
from app.contact.contact_module import contact_module
from app.auth import auth_check, get_userid
from app import socketio
from flask_socketio import join_room

contact_handler = Blueprint('contact_handler', __name__)

@contact_handler.route('/messages' , methods=['GET'])
@auth_check()
def contact_message_route(userid = -1):
    msg = contact_module.get_user_msgs(userid)
    return jsonify(msg)

@contact_handler.route('/sendmsg' , methods=['POST'])
@auth_check()
def contact_sendmsg_route(userid = -1):
    request_json = request.json
    request_json['send_userid'] = userid
    msg = contact_module.send_msg(request_json)
    return jsonify(msg)


@contact_handler.route('/chatroom' , methods=['POST'])
@auth_check()
def contact_chatroom_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = contact_module.query_chatroom(request_json)
    return jsonify(msg)

@contact_handler.route('/newchat' , methods=['POST'])
@auth_check()
def contact_newchat_route(userid = -1):
    request_json = request.json
    request_json['userid'] = userid
    msg = contact_module.create_chatroom(request_json)
    return jsonify(msg)

@socketio.on('join_chatroom',namespace='/chat_socket')
def user_join_chatroom(data):
    userid = get_userid(data.get('token', ''))
    chatrooms = data.get('chatrooms', [])
    for chatroom in chatrooms:
        chatroomid = chatroom.get('chatroomid', -1)
        if userid > 0 and chatroomid > 0:
            #验证user 是否在 chatroom
            join_room(chatroomid)