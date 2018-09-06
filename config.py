import os

class Config:
    '''
    parent class
    '''
    pass

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