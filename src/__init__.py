from flask import Flask, jsonify
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DB_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JWT_SECRET_KEY']=os.environ.get('JWT_SECRET_KEY')
JWTManager(app)
db.app = app
db.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(bookmarks)


