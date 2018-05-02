from app import db
from app.suggest.models.suggest_model import suggest_model
from app.user.models.user_model import user_model
from app.error import ERROR
from app.json_format import models_format_json

class suggest_module:
    @staticmethod
    def create_suggest(request):
        userid = request.get('userid', -1)
        title = request.get('title', '')
        content = request.get('content', '')
        if title and content:
            newsuggest = suggest_model(userid, title, content)
            db.session.add(newsuggest)
            db.session.commit()

            user_model.send_mail_by_userid(userid, "建议收到通知", "学生会已收到您的建议,会尽快进行处理!")
            return ERROR.success(newsuggest.to_json())
        return ERROR.REQUEST_INVALID

    @staticmethod
    def query_user_suggestions(userid):
        user = user_model.find_by_id(userid)
        return ERROR.success(models_format_json(user.suggestions,  'suggestions'))

    @staticmethod
    def query_suggestion(request):
        userid = request.get('userid', -1)
        suggestid = request.get('suggestid', -1)

        suggestion = suggest_model.find_by_id(suggestid)
        if suggestion:
            if suggestion.userid == userid:
                return ERROR.success(suggestion.to_json())
            return ERROR.PERMISSION_DENIED
        return ERROR.SUGGESTION_NOT_FOUND