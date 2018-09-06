import os

class Config:
    '''
    parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:dan15done@localhost/pitch'

class ProdConfig(Config):
    '''
    production configurations child class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
 'development': DevConfig,
 'production': ProdConfig
}