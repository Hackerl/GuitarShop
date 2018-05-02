from app import db
from datetime import datetime
from app.model_base import model_base

class issue_model(model_base, db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(500), nullable=False, default='')
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, userid, title, content):
        self.userid = userid
        self.title = title
        self.content= content

    def set_status(self, status, comment):
        self.status = status
        self.comment = comment
        self.update_time = datetime.now()

    def to_json(self, columns=['id', 'userid', 'title', 'content', 'comment', 'status', 'create_time', 'update_time']):
        return super().to_json(self, columns)