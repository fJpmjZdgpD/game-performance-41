import os

class Config:
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

    @classmethod
    def init_app(cls, app):
        app.config['DEBUG'] = cls.DEBUG
        app.config['SQLALCHEMY_DATABASE_URI'] = cls.DATABASE_URI
        app.config['SECRET_KEY'] = cls.SECRET_KEY
        app.config['ALLOWED_HOSTS'] = cls.ALLOWED_HOSTS

