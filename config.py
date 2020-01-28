import os

class Config:
    # General
    TESTING = True
    FLASK_DEBUG = True
    THREADS_PER_PAGE = 2
    SECRET_KEY = os.environ.get('SECRET_KEY')
   
    # Database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
