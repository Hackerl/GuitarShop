from app import db
from datetime import datetime
from app.model_base import model_base
import json

class class_model(model_base, db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    teaching_type = db.Column(db.String(100), nullable=False)
    teaching_address = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    class_count = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False, default='')
    files = db.Column(db.Text, nullable=False)
    introduction = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(500), nullable=False, default='')

    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    columns_to_json = ['id', 'userid', 'name', 'type', 'rank', 'teaching_type',
                       'teaching_address', 'price', 'discount', 'class_count',
                       'content', 'files', 'introduction','create_time', 'update_time']

    def __init__(self, userid, name, type, rank, teaching_type, teaching_address, price, discount, class_count, content, files, introduction):
        self.userid = userid
        self.name = name
        self.type = type
        self.rank = rank
        self.teaching_type = teaching_type
        self.teaching_address = teaching_address
        self.price = price
        self.discount = discount
        self.class_count = class_count
        self.content = content
        self.introduction = introduction
        self.files= json.dumps(files)

    def update(self, name, type, rank, teaching_type, teaching_address, price, discount, class_count, content, files, introduction):
        self.name = name
        self.type = type
        self.rank = rank
        self.teaching_type = teaching_type
        self.teaching_address = teaching_address
        self.price = price
        self.discount = discount
        self.class_count = class_count
        self.content = content
        self.introduction = introduction
        self.files= json.dumps(files)
        self.update_time = datetime.now()

    def to_json(self, columns=[]):
        task_json = super(class_model, self).to_json(columns = columns)
        files = task_json.get('files', '{}')
        task_json['files'] = json.loads(files)
        return task_json

    def set_status(self, status, comment):
        self.status = status
        self.comment = comment
        self.update_time = datetime.now()