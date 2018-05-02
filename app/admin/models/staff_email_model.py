from app import db, mail
from datetime import datetime
from app.model_base import model_base
from flask_mail import Message

class staff_model(model_base, db.Model):
    __tablename__ = 'staff_emails'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    columns_to_json = ['id', 'name', 'email', 'create_time']

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def send_mail_to_staff(cls, _subject, _body):
        staffs = cls.query.all()
        with mail.connect() as conn:
            for staff in staffs:
                msg = Message( rsubject=_subject,
                               body=_body,
                               ecipients=[staff.email]
                             )
                conn.send(msg)

