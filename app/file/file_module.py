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
            realname = os.path.basename(file.filename)
            (rawname, extension) = os.path.splitext(realname)

            file.filename = 'picture_name'
            filename = photos.save(file, 'picture', name='%s.%s' % (datetime.now().isoformat(), extension))
            file_url = photos.url(filename)
            return ERROR.success({'filename':realname, 'picture_url': file_url})

        except UploadNotAllowed:
            return ERROR.UPLOAD_FAILD