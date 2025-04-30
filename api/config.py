from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", default=False)
    FLASK_APP = os.getenv("FLASK_APP", default="app.py")
    FLASK_ENV = os.getenv("FLASK_ENV", default="development")