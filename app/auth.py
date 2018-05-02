from flask import request, current_app, jsonify
from app.error import ERROR
from itsdangerous import BadTimeSignature, SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.user.models.user_model import user_model
from functools import wraps

class auth_module:
    level_define = {
        'ADMIN_LEVEL' : 0,
        'USER_LEVEL' : 1
    }

    @staticmethod
    def verify_token(level = 1):
        def outwrapper(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                token = request.cookies.get("token", '')
                if token:
                    serializer = Serializer(current_app.config['SECRET_KEY'])
                    try:
                        user = serializer.loads(token)
                        userid = user.get('userid', -1)
                        if auth_module.permission(userid, level):
                            kwargs['userid'] = userid
                            return func(*args, **kwargs)
                    except BadSignature as e:
                        pass
                    except SignatureExpired as e:
                        pass
                    except BadTimeSignature as e:
                        pass
                return jsonify(ERROR.NEED_AUTH)
            return wrapper
        return outwrapper

    @staticmethod
    def get_userid_from_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            user = serializer.loads(token)
            userid = user.get('userid', -1)
            return userid
        except BadSignature as e:
            return -1
        except SignatureExpired as e:
            return -1
        except BadTimeSignature as e:
            return -1

    @staticmethod
    def permission(userid, level):
        user = user_model.find_by_id(userid)
        if user:
            return user.level <= level
        else:
            return False

auth_check = auth_module.verify_token
get_userid = auth_module.get_userid_from_token
level_define = auth_module.level_define