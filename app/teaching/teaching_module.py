from app import db
from app.teaching.models.class_model import class_model
from app.user.models.user_model import user_model
from app.error import ERROR

class teaching_module:
    @staticmethod
    def create_class(request):
        userid = request.get('userid', -1)
        name = request.get('name', '')
        type = request.get('type', '')
        rank = request.get('rank', -1)
        teaching_type = request.get('teaching_type', '')
        teaching_address = request.get('teaching_address', '')
        price = request.get('price', -1)
        discount = request.get('discount', -1)
        class_count = request.get('class_count', 16)
        files = request.get('files', [])
        introduction = request.get('introduction', '')

        if name and files:
            newclass = class_model(userid, name, type, rank, teaching_type, teaching_address, price, discount, class_count, files, introduction)
            db.session.add(newclass)
            db.session.commit()

            user_model.send_mail_by_userid(userid, "开设课程通知", "成功开设课程!")
            return ERROR.success(newclass.to_json())
        return ERROR.REQUEST_INVALID

    @staticmethod
    def query_class(request):
        classid = request.get('classid', -1)
        _class = class_model.find_by_id(classid)
        if _class:
            return ERROR.success(_class.to_json())
        else:
            return ERROR.ISSUE_NOT_FOUND

    @staticmethod
    def query_user_classes(userid):
        user = user_model.find_by_id(userid)
        return ERROR.success({'classes': [_class.to_json() for _class in user.classes]})

    @staticmethod
    def del_class(request):
        classid = request.get('classid', -1)
        userid = request.get('userid', -1)
        _class = class_model.find_by_id(classid)
        if _class:
            if _class.user.id == userid:
                db.session.delete(_class)
                return ERROR.SUCCESS
            return ERROR.PERMISSION_DENIED
        return ERROR.class_NOT_FOUND