from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser
from flask_login import LoginManager


db = SQLAlchemy()

config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")

DB_USER = config["database"]["DB_USER"]
DB_PASSWORD = config["database"]["DB_PASSWORD"]
DB_HOST = config["database"]["DB_HOST"]
DB_PORT = config["database"]["DB_PORT"]
DB_NAME = config["database"]["DB_NAME"]


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config['database']['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    with app.app_context():
        db.create_all()
    print("Tables Created!")

