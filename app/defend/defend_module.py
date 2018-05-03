from app import db
from app.defend.models.issue_model import issue_model
from app.user.models.user_model import user_model
from app.error import ERROR

class defend_module:
    @staticmethod
    def create_issue(request):
        userid = request.get('userid', -1)
        type = request.get('type', '')
        files = request.get('files', '')
        if type and files:
            newissue = issue_model(userid, type, files)
            db.session.add(newissue)
            db.session.commit()

            user_model.send_mail_by_userid(userid, "认证进度通知", "管理员已收到您的认证信息请求,会尽快进行处理!")
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
        return ERROR.success({'issues': [issue.to_json(columns=['type', 'comment', 'status']) for issue in user.issues]})

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