from app import db
from app.defend.models.issue_model import issue_model
from app.user.models.user_model import user_model
from app.error import ERROR
from app.json_format import models_format_json

class defend_module:
    @staticmethod
    def create_issue(request):
        userid = request.get('userid', -1)
        title = request.get('title', '')
        content = request.get('content', '')
        if title and content:
            newissue = issue_model(userid, title, content)
            db.session.add(newissue)
            db.session.commit()

            user_model.send_mail_by_userid(userid, "维权进度通知", "学生会已收到您的维权信息,会尽快进行处理!")
            return ERROR.success(newissue.to_json())
        return ERROR.REQUEST_INVALID

    @staticmethod
    def query_issue(request):
        issueid = request.get('issueid', -1)
        issue = issue_model.find_by_id(issueid)
        if issue:
            return ERROR.success(issue.to_json())
        else:
            return ERROR.ISSUE_NOT_FOUND

    @staticmethod
    def query_user_issues(userid):
        user = user_model.find_by_id(userid)
        return ERROR.success(models_format_json(user.issues,  'issues', columns=['title', 'comment', 'status']))

    @staticmethod
    def del_issue(request):
        issueid = request.get('issueid', -1)
        userid = request.get('userid', -1)
        issue = issue_model.find_by_id(issueid)
        if issue:
            if issue.user.id == userid:
                db.session.delete(issue)
                return ERROR.SUCCESS
            return ERROR.PERMISSION_DENIED
        return ERROR.ISSUE_NOT_FOUND