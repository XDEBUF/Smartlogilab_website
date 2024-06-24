import os
from dotenv import load_dotenv
#basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()
class Config:
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'pptx', 'xlsx'}
    SECRET_KEY = 'bye'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False