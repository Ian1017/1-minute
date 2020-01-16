import os

class Config:
    '''
    General configuration parent
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/P'


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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/P'


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General Configuration Settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:diamonds@localhost/P'


    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}