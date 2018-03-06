class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
