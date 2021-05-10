import os


BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# /home/mateus/Documentos/GitHub/Flask/flask_blog/app/config.py


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =   'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
