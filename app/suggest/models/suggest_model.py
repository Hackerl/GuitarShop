from app import db
from datetime import datetime
from app.model_base import model_base

class suggest_model(model_base, db.Model):
    __tablename__ = 'suggests'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, userid, title, content):
        self.userid = userid
        self.title = title
        self.content = content

    def to_json(self, columns=['id', 'userid', 'title', 'content', 'create_time']):
        return super().to_json(self, columns)