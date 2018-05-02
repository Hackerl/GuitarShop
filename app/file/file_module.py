from app import photos
from app.error import ERROR
from flask_uploads import UploadNotAllowed
from datetime import datetime
import os

class file_module:
    @staticmethod
    def upload_file(request_files):
        try:
            file = request_files['file']
            realname = file.filename
            filename = photos.save(file, 'picture', name='%s.%s' % (datetime.now().isoformat(), os.path.splitext(realname)[-1]))
            file_url = photos.url(filename)
            return ERROR.success({'filename':realname, 'picture_url': file_url})
        except UploadNotAllowed:
            return ERROR.UPLOAD_FAILD