from app import db
from datetime import datetime
from app.model_base import model_base

class message_model(model_base, db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    chatroomid = db.Column(db.Integer, db.ForeignKey('chatrooms.id'))
    send_userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String(500), nullable=False)
    type = db.Column(db.Integer, nullable=False, default= 0)
    send_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, chatroomid, send_userid, content, type):
        self.chatroomid = chatroomid
        self.send_userid = send_userid
        self.content = content
        self.type = type

    def to_json(self, columns=['id', 'send_userid', 'recv_userid', 'content', 'type', 'send_time']):
        return super().to_json(self, columns)

