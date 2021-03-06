import os


class Config:
    '''
    General configuration parent
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/minute'
    UPLOADED_PHOTOS_DEST = 'app/static'
    SECRET_KEY = '69df8b1b7481455e9e27bb627a473aaf'
   
    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration with general configuration class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/minute'


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General Configuration Settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/minute'


    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
