from app import db
from app.wiki.models.question_model import question_model
from app.error import ERROR
from sqlalchemy import or_

class wiki_module:
    @staticmethod
    def create_question(request):
        title = request.get('title', '')
        content = request.get('content', '')
        if content:
            newquestion = question_model(title, content)
            db.session.add(newquestion)
            db.session.commit()
            return ERROR.success(newquestion.to_json())
        else:
            return ERROR.REQUEST_INVALID

    @staticmethod
    def query_question(request):
        questionid = request.get('questionid', '')
        question = question_model.find_by_id(questionid)
        if question:
            return ERROR.success(question.to_json())
        else:
            return ERROR.QUESTION_NOT_FOUND

    @staticmethod
    def get_all_questions():
        return ERROR.success({'questions': [question.to_json() for question in question_model.query.all()]})

    @staticmethod
    def search_question(request):
        keyword = request.get('keyword', '')
        questions = question_model.query.filter( or_(
                                    question_model.title.like('%' + keyword + '%'),
                                    question_model.content.like('%' + keyword + '%')
                                    )).all()
        return ERROR.success({'questions': [question.to_json() for question in questions]})

    @staticmethod
    def del_question(request):
        questionid = request.get('questionid', -1)
        question = question_model.find_by_id(questionid)
        if question:
            db.session.delete(question)
            return ERROR.SUCCESS
        else:
            return ERROR.QUESTION_NOT_FOUND