from flask import Flask, jsonify, redirect
from src.auth import auth
from src.bookmarks import bookmarks
from src.constants.http_status_codes import HTTP_404_NOT_FOUND
from src.database import db, Bookmarks
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
@app.get('/<short_url>')
def redirect_to_url(short_url):
  bookmark = Bookmarks.query.filter_by(short_url=short_url).first_or_404()

  if bookmark:
    bookmark.visits = bookmark.visits + 1
    db.session.commit()

    return redirect(bookmark.url)

@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
  return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

