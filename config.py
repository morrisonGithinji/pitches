import os

class Config:

    SECRET_KEY="just a key"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ebay:qwerty@localhost/pitches'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ebay:qwerty@localhost/pitches_test'    

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}