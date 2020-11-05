import os
class Config:
    SECRET_KEY="64f4bcf6-fca5-44f8-b51e-d3aef83726ed"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://wambui:neema@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    '''
    mail config
    '''
    DEBUG=False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL=True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://wambui:neema@localhost/blog'
class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://wambui:neema@localhost/blog'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://wambui:neema@localhost/blog'


config_options={
'development':DevConfig,
"production":ProdConfig,
"test":TestConfig
}
