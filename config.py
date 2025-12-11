import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-secret-key-12345'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Mail settings (simulated for now or ready for real SMTP)
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
