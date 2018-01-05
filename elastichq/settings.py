import os


class Config(object):
    SECRET_KEY = os.environ.get('ELASTICHQ_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    DB_USERNAME = os.environ.get('ELASTICHQ_DB_USERNAME')
    DB_PASSWORD = os.environ.get('ELASTICHQ_DB_PASSWORD')
    DB_HOSTNAME = os.environ.get('ELASTICHQ_DB_HOSTNAME')
    DB_DATABASE = os.environ.get('ELASTICHQ_DB_DATABASE')
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:5432/%s' % (
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOSTNAME,
        DB_DATABASE
    )


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    DB_NAME = 'test.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
