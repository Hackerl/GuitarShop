from app import db
from app.contact.models.message_model import message_model
from app.contact.models.chat_model import chatroom_model, chatroom_record_model
from app.user.models.user_model import user_model
from app.error import ERROR
from app import socketio

class contact_module:
    @staticmethod
    def send_msg(request):
        send_userid = request.get('send_userid', -1)
        chatid = request.get('chatid', -1)
        content = request.get('content', '')
        type = request.get('type', '')
        chatroom = chatroom_model.find_by_id(chatid)

        if chatroom:
            chatroom_users = {'users': [user.to_json() for user in chatroom.get_users()]}
            for user in chatroom_users['users']:
                if send_userid == user['id']:
                    # 更新访问时间
                    chatroom_record_model.visit_chatroom(send_userid, chatid)

                    new_msg = message_model(chatid, send_userid, content, type)
                    db.session.add(new_msg)
                    db.session.commit()

                    broad_new_msg = new_msg.to_json()
                    broad_new_msg['chatid'] = chatid
                    broad_new_msg.update(user_model.find_by_id(send_userid).to_json(columns = ['id', 'username', 'head']))
                    socketio.emit('new_msg',broad_new_msg, namespace='/chat_socket', room=chatid)
                    return ERROR.SUCCESS
            return ERROR.PERMISSION_DENIED
        else:
            return ERROR.CHAT_NOT_FOUND

    @staticmethod
    def get_user_msgs(userid):
        user = user_model.find_by_id(userid)
        chats= {"chats": []}

        for chatroom_record in user.chatroom_records:
            last_visit_time = chatroom_record.last_visit_time
            chatroom = chatroom_record.chatroom
            room = {"chatroom": chatroom.to_json()}

            new_msg_num = chatroom.messages.filter(message_model.send_time > last_visit_time).count()
            room.update({"new_num": new_msg_num})

            for user in chatroom.get_users():
                if user.id != userid:
                    room.update({"name": user.username, "head": user.head})

            chats['chats'].append(room)
        return ERROR.success(chats)

    @staticmethod
    def create_chatroom(request):
        userid = request.get('userid', -1)
        invited_userid = request.get('invited_userid', -1)

        user = user_model.find_by_id(userid)
        invited_user = user_model.find_by_id(invited_userid)
        if invited_user:
            new_chatroom = chatroom_model()
            db.session.add(new_chatroom)
            db.session.commit()
            chatroom_record_model.create_chatroom_record(userid, invited_userid, new_chatroom.id)

            return ERROR.success(new_chatroom.to_json())
        else:
            return ERROR.USER_NOT_FOUND

    @staticmethod
    def query_chatroom(request):
        userid = request.get('userid', -1)
        chatid = request.get('chatid', -1)

        chatroom = chatroom_model.find_by_id(chatid)
        if chatroom:
            chatroom_all_users = {}
            for user in chatroom.get_users():
                chatroom_all_users[user.id] = user.to_json(columns = ['id', 'username', 'head'])

            if userid in chatroom_all_users:
                # 更新访问时间
                chatroom_record_model.visit_chatroom(userid, chatid)

                msgs = {'messages': [message.to_json() for message in chatroom.messages]}
                for msg in msgs['messages']:
                    msg.update(chatroom_all_users.get(msg['send_userid'], {}))
                return ERROR.success(msgs)
            return ERROR.PERMISSION_DENIED
        else:
            return ERROR.CHAT_NOT_FOUND