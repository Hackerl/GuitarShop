class ERROR:
    SUCCESS = {'error' : 0 ,'msg': 'success'}
    NO_JSON = {'error' : -1 ,'msg': 'no json'}
    NEED_AUTH = {'error' : -2 ,'msg': 'please auth first'}
    REQUEST_INVALID = {'error' : -3 ,'msg': 'request invalid'}
    AUTH_FAILD = {'error' : -4 ,'msg': 'username or password invalid'}
    USER_EXIST = {'error' : -5 ,'msg': 'user exists'}
    ISSUE_NOT_FOUND = {'error' : -6 ,'msg': 'issue not find'}
    USER_NOT_FOUND = {'error' : -7 ,'msg': 'user not find'}
    CHAT_NOT_FOUND = {'error': -8, 'msg': 'chat not find'}
    OLD_PWD_ERROR = {'error': -9, 'msg': 'old password error'}
    PERMISSION_DENIED = {'error': -10, 'msg': 'permission denied'}
    QUESTION_NOT_FOUND = {'error': -11, 'msg': 'question not found'}
    EMAIL_NOT_FOUND = {'error': -11, 'msg': 'email not found'}
    HEAD_IS_NONE = {'error': -11, 'msg': 'head url is none'}
    UPLOAD_FAILD = {'error': -12, 'msg': 'upload faild! please check extension of the picture file'}
    EMAIL_FORMAT_ERROR = {'error': -13, 'msg': 'email format error'}
    SUGGESTION_NOT_FOUND = {'error': -14, 'msg': 'suggestion not found'}
    EMAIL_EXIST = {'error': -15, 'msg': 'email exist'}
    PASSWORD_SHORT = {'error': -16, 'msg': 'password length greater than 8'}
    CLASS_NOT_FOUND = {'error': -17, 'msg': 'class not find'}

    @staticmethod
    def success(r_json):
        r_json.update(ERROR.SUCCESS)
        return r_json
