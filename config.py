import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_BINDS = {
        'innobid':'mysql://innobid:dmdcjs0@127.0.0.1/innobid?charset=utf8',
        'innoMVA':'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    }


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_BINDS = {
        'innobid':'mysql://innobid:dmdcjs0@127.0.0.1/innobid?charset=utf8',
        'innoMVA':'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    }


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}