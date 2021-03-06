from app import db
from datetime import datetime
from app.model_base import model_base

class question_model(model_base, db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    columns_to_json = ['id', 'userid', 'title', 'content', 'create_time']

    def __init__(self, title, content):
        self.title = title
        self.content = content