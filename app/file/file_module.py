from app import photos
from app.error import ERROR
from flask_uploads import UploadNotAllowed

class file_module:
    @staticmethod
    def upload_file(request_files):
        try:
            filename = photos.save(request_files['file'], 'picture')
            file_url = photos.url(filename)
            return ERROR.success({'picture_url': file_url})
        except UploadNotAllowed:
            return ERROR.UPLOAD_FAILD