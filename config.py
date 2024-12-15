import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'defaultsecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:sam@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('craftedvisualsstudio')
    MAIL_PASSWORD = os.environ.get('MohamedSham')
