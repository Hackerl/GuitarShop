from app import db, mail
from datetime import datetime
from app.model_base import model_base
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

class user_model(model_base, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(30), nullable=True)
    realname = db.Column(db.String(50), nullable=True)
    head = db.Column(db.String(200), nullable=False, default='/img/user.jpeg')
    level = db.Column(db.Integer, default=1)
    create_time = db.Column(db.DateTime, default=datetime.now)
    last_time = db.Column(db.DateTime, default=datetime.now)
    issues = db.relationship('issue_model', backref='user')
    chatroom_records = db.relationship("chatroom_record_model", backref="user")
    suggestions = db.relationship('suggest_model', backref='user')

    teaching_address = db.Column(db.String(500), nullable=True)
    major = db.Column(db.String(50), nullable=True)
    introduction = db.Column(db.String(1000), nullable=True)
    additional_server = db.Column(db.String(500), nullable=True)

    columns_to_json = ['id', 'username', 'head', 'phone', 'email', 'create_time']

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash= generate_password_hash(password)
        self.email = email

    def reset_password(self, newpassword):
        self.password_hash = generate_password_hash(newpassword)

    def check_password(self, oldpassword):
        return check_password_hash(self.password_hash, oldpassword)

    @classmethod
    def verify_user(cls, _username, _password):
        user = cls.query.filter_by(username = _username).first()
        if user:
            if check_password_hash(user.password_hash, _password):
                return user.id
        return -1

    @classmethod
    def verify_user_by_eamil(cls, _email, _password):
        user = cls.query.filter_by(email = _email).first()
        if user:
            if check_password_hash(user.password_hash, _password):
                return user.id
        return -1

    @classmethod
    def user_exist(cls, _username):
        user = cls.query.filter_by(username = _username).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def email_exist(cls, _email):
        user = cls.query.filter_by(email = _email).first()
        if user:
            return True
        else:
            return False

    @classmethod
    def send_mail_by_userid(cls, userid, _subject, _body):
        user = cls.query.filter_by(id=userid).first()
        msg = Message(subject=_subject,
                      body = _body,
                      recipients=[user.email])
        mail.send(msg)

    def set_info(self, username, email, phone, realname):
        self.username = username
        self.email = email
        self.phone = phone
        self.realname = realname

    def set_server_info(self, teaching_address, major, introduction, additional_server):
        self.teaching_address = teaching_address
        self.major = major
        self.introduction = introduction
        self.additional_server = additional_server

    def get_chatrooms(self):
        chatrooms = []
        for chatroom_record in self.chatroom_records:
            chatrooms.append(chatroom_record.chatroom)
        return chatrooms