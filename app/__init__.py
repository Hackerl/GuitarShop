from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()
mail = Mail()
photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.user.user_blueprint import user_handler as user_blueprint
    app.register_blueprint(user_blueprint,  url_prefix='/user')

    from app.defend.defend_blueprint import defend_handler as defend_blueprint
    app.register_blueprint(defend_blueprint,  url_prefix='/check')

    from app.contact.contact_blueprint import contact_handler as contact_blueprint
    app.register_blueprint(contact_blueprint,  url_prefix='/contact')

    from app.admin.admin_blueprint import admin_handler as admin_blueprint
    app.register_blueprint(admin_blueprint,  url_prefix='/admin')

    from app.suggest.suggest_blueprint import suggest_handler as suggest_blueprint
    app.register_blueprint(suggest_blueprint,  url_prefix='/suggest')

    from app.wiki.wiki_blueprint import wiki_handler as wiki_blueprint
    app.register_blueprint(wiki_blueprint,  url_prefix='/wiki')

    from app.file.file_blueprint import file_handler as file_blueprint
    app.register_blueprint(file_blueprint,  url_prefix='/file')

    from app.teaching.teaching_blueprint import teaching_handler as teaching_blueprint
    app.register_blueprint(teaching_blueprint,  url_prefix='/teaching')

    db.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)

    configure_uploads(app, photos)
    patch_request_class(app)

    CORS(app, supports_credentials=True)

    return app, socketio
