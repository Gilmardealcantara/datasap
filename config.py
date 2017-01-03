# Students' Academic Performance
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres:///datasap'


class Testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


