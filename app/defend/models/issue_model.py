from app import db
from datetime import datetime
from app.model_base import model_base
import json
class issue_model(model_base, db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.Integer, nullable=False)
    files = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(500), nullable=False, default='')
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    columns_to_json = ['id', 'userid', 'type', 'files', 'comment', 'status', 'create_time', 'update_time']

    def __init__(self, userid, type, files):
        self.userid = userid
        self.type = type
        self.files= json.dumps(files)

    def set_status(self, status, comment):
        self.status = status
        self.comment = comment
        self.update_time = datetime.now()

    def to_json(self, columns=[]):
        task_json = super(issue_model, self).to_json(columns = columns)
        files = task_json.get('files', '{}')
        task_json['files'] = json.loads(files)
        return task_json