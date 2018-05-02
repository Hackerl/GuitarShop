from app import db
from datetime import datetime
from app.model_base import model_base

class chatroom_record_model(model_base, db.Model):
    __tablename__ = 'chatroom_records'
    userid = db.Column('userid', db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    chatroomid = db.Column('chatroomid', db.Integer, db.ForeignKey('chatrooms.id'), nullable=False, primary_key=True)
    last_visit_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, userid, chatroomid):
        self.userid = userid
        self.chatroomid = chatroomid

    @classmethod
    def visit_chatroom(cls, userid_, chatid_):
        chatroom_record = cls.query.filter_by(userid=userid_, chatroomid=chatid_).first()
        chatroom_record.last_visit_time = datetime.now()

    @staticmethod
    def create_chatroom_record(userid_1, userid_2, chatroomid):
        new_chatroom_record = chatroom_record_model(userid_1, chatroomid)
        new_chatroom_record_ = chatroom_record_model(userid_2, chatroomid)
        db.session.add(new_chatroom_record)
        db.session.add(new_chatroom_record_)


class chatroom_model(model_base, db.Model):
    __tablename__ = 'chatrooms'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    messages = db.relationship('message_model', backref='chatroom', lazy='dynamic')
    chatroom_records = db.relationship("chatroom_record_model", backref="chatroom")

    columns_to_json = ['id', 'create_time']

    def get_users(self):
        users = []
        for chatroom_record in self.chatroom_records:
            users.append(chatroom_record.user)
        return users