from app import db, photos
from app.user.models.user_model import user_model
from app.contact.models.chat_model import chatroom_model, chatroom_record_model
from app.contact.models.message_model import message_model
from app.error import ERROR
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import re

email_r = r"^[a-z_0-9.-]{1,64}@([a-z0-9-]{1,200}.){1,5}[a-z]{1,6}$"

class user_module:
    @staticmethod
    def login(request):
        username = request.get('username','')
        password = request.get('password','')

        if username and password and len(password) >= 8:
            userid = user_model.verify_user_by_eamil(username, password) if re.match(email_r, username) else user_model.verify_user(username, password)
            if userid > 0:
                serializer = Serializer(current_app.config['SECRET_KEY'], expires_in = 864000)
                token = serializer.dumps({'userid': userid})
                return True, ERROR.SUCCESS, token

        return False, ERROR.AUTH_FAILD, None

    @staticmethod
    def register(request):
        username = request.get('username', '')
        password = request.get('password', '')
        email = request.get('email', '')
        if len(password) >= 8 and username:
            if re.match(email_r, email):
                if not user_model.user_exist(username):
                    if not user_model.email_exist(email):
                        newuser = user_model(username, password, email)
                        db.session.add(newuser)
                        db.session.commit()

                        if newuser.id != 1:
                            new_chatroom = chatroom_model()
                            db.session.add(new_chatroom)
                            db.session.commit()
                            chatroom_record_model.create_chatroom_record(newuser.id, 1, new_chatroom.id)

                            new_msg = message_model(new_chatroom.id, 1, "欢迎来到香樟活宝的维权平台,有任何问题都可以询问我", 0)
                            db.session.add(new_msg)
                        return ERROR.SUCCESS
                    return ERROR.EMAIL_EXIST
                return ERROR.USER_EXIST
            return ERROR.EMAIL_FORMAT_ERROR
        return ERROR.PASSWORD_SHORT


    @staticmethod
    def getinfo(userid):
        user = user_model.find_by_id(userid)
        return ERROR.success(user.to_json(columns = ['id', 'username', 'head', 'phone', 'email',
                                                     'realname', 'teaching_address', 'major', 'introduction',
                                                     'additional_server', 'level', 'create_time']))
    @staticmethod
    def reset_password(request):
        oldpassword = request.get('oldpassword', '')
        newpassword = request.get('newpassword', '')
        userid = request.get('userid', -1)

        user = user_model.find_by_id(userid)
        if len(newpassword) >= 8:
            if user.check_password(oldpassword):
                user.reset_password(newpassword)
                return ERROR.SUCCESS
            return ERROR.OLD_PWD_ERROR
        return ERROR.PASSWORD_SHORT

    @staticmethod
    def set_user_info(request):
        newusername = request.get('username', '')
        email = request.get('email', '')
        phone = request.get('phone', '')
        realname = request.get('realname', '')
        userid = request.get('userid', -1)

        user = user_model.find_by_id(userid)
        if re.match(email_r, email):
            if user.username == newusername or not user_model.user_exist(newusername):
                user.set_info(newusername, email, phone, realname)
                return ERROR.SUCCESS
            else:
                return ERROR.USER_EXIST
        return ERROR.EMAIL_FORMAT_ERROR

    @staticmethod
    def set_server_info(request):
        teaching_address = request.get('teaching_address', '')
        major = request.get('major', '')
        introduction = request.get('introduction', '')
        additional_server = request.get('additional_server', '')
        userid = request.get('userid', -1)

        user = user_model.find_by_id(userid)
        user.set_server_info(teaching_address, major, introduction, additional_server)
        return ERROR.SUCCESS

    @staticmethod
    def set_user_head(request):
        head_url = request.get('head_url', '')
        userid = request.get('userid', -1)
        user = user_model.find_by_id(userid)
        if head_url:
            user.head = head_url
            return ERROR.SUCCESS
        else:
            return ERROR.HEAD_IS_NONE