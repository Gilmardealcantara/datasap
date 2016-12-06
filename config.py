from os import getcwd, path

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(getcwd(), 'data/database.sqlite')
    QLALCHEMY_DATABASE_URI = "postgresql://gilmar:123456@localhost/gilmar"


class Testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
