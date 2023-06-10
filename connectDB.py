from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()
app= Flask(__name__)


secret_key = os.getenv("SECRET_KEY")
database_url = os.getenv("DB_URI")

app.secret_key=secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)