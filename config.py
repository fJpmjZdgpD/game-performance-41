import os

class Config:
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
    MAX_CONNECTIONS = int(os.getenv('MAX_CONNECTIONS', 100))

    @staticmethod
    def init_app(app):
        app.config['DEBUG'] = Config.DEBUG
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
        app.config['SECRET_KEY'] = Config.SECRET_KEY
        app.config['MAX_CONNECTIONS'] = Config.MAX_CONNECTIONS
        
    @classmethod
    def from_env(cls):
        return cls()

config = Config.from_env()