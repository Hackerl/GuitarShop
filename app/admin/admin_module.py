from app import db
from app.defend.models.issue_model import issue_model
from app.suggest.models.suggest_model import suggest_model
from app.admin.models.staff_email_model import staff_model
from app.user.models.user_model import user_model
from app.teaching.models.class_model import class_model
from app.error import ERROR

class admin_module:
    @staticmethod
    def update_issue(request):
        issueid = request.get('issueid', -1)
        status = request.get('status', -1)
        comment = request.get('comment', '')
        issue = issue_model.find_by_id(issueid)
        if issue:
            issue.set_status(status, comment)
            if status == -1:
                email_msg = '审核未通过!\n\n回复:\n    '
            else:
                email_msg = '审核通过!\n\n回复:\n    '
            user_model.send_mail_by_userid(issue.userid, "认证进度通知", email_msg + comment)
            return ERROR.SUCCESS
        else:
            return ERROR.ISSUE_NOT_FOUND

    @staticmethod
    def delete_issue(request):
        issueid = request.get('issueid', -1)
        issue = issue_model.find_by_id(issueid)
        if issue:
            db.session.delete(issue)
            return ERROR.SUCCESS
        else:
            return ERROR.ISSUE_NOT_FOUND

    @staticmethod
    def get_issue_content(request):
        issueid = request.get('issueid', -1)
        issue = issue_model.find_by_id(issueid)
        if issue:
            return ERROR.success(issue.to_json(columns = ['files']))
        else:
            return ERROR.ISSUE_NOT_FOUND

    @staticmethod
    def get_user_info(request):
        userid = request.get('userid', -1)
        user = user_model.find_by_id(userid)
        if user:
            return ERROR.success(user.to_json(columns = ['id', 'username', 'head', 'phone', 'email',
                                                         'realname', 'teaching_address', 'major', 'introduction',
                                                         'wechat', 'additional_server', 'level', 'create_time']))
        else:
            return ERROR.USER_NOT_FOUND

    @staticmethod
    def get_all_issues():
        return ERROR.success({'issues': [issue.to_json(columns=['id', 'userid', 'type', 'status']) for issue in issue_model.query.all()]})

    @staticmethod
    def get_all_suggestions():
        return ERROR.success({'suggestions': [suggest.to_json(columns=['id', 'title', 'status']) for suggest in suggest_model.query.all()]})

    @staticmethod
    def get_suggestion_content(request):
        suggestid = request.get('suggestid', -1)
        suggestion = suggest_model.find_by_id(suggestid)
        if suggestion:
            return ERROR.success(suggestion.to_json(columns = ['content']))
        else:
            return ERROR.SUGGESTION_NOT_FOUND

    @staticmethod
    def get_staffs():
        return ERROR.success({'staffs': [staff.to_json(columns=['id', 'name', 'email']) for staff in staff_model.query.all()]})

    @staticmethod
    def add_staff(request):
        name = request.get('name', '')
        email = request.get('email', '')
        if name and email:
            new_staff =  staff_model(name, email)
            db.session.add(new_staff)
            db.session.commit()
            return ERROR.success(new_staff.to_json())
        else:
            return ERROR.REQUEST_INVALID

    @staticmethod
    def del_staff(request):
        staffid = request.get('staffid', -1)
        staff = staff_model.find_by_id(staffid)
        if staff:
            db.session.delete(staff)
            return ERROR.SUCCESS
        else:
            return ERROR.EMAIL_NOT_FOUND

    @staticmethod
    def get_all_classes():
        return ERROR.success({'classes': [_class.to_json(columns=['id', 'userid', 'name', 'status']) for _class in class_model.query.all()]})

    @staticmethod
    def update_class(request):
        classid = request.get('classid', -1)
        status = request.get('status', -1)
        comment = request.get('comment', '')
        _classid = class_model.find_by_id(classid)
        if _classid:
            _classid.set_status(status, comment)
            if status == -1:
                email_msg = '审核未通过!\n\n回复:\n    '
            else:
                email_msg = '审核通过!\n\n回复:\n    '
            user_model.send_mail_by_userid(_classid.userid, "开店审核通知", email_msg + comment )
            return ERROR.SUCCESS
        else:
            return ERROR.CLASS_NOT_FOUND

    @staticmethod
    def delete_class(request):
        classid = request.get('classid', -1)
        _classid = class_model.find_by_id(classid)
        if _classid:
            db.session.delete(_classid)
            return ERROR.SUCCESS
        else:
            return ERROR.CLASS_NOT_FOUND