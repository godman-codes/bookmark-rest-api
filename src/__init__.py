from flask import Flask, jsonify
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
app.config['SECRET_KEY'] = 'bucduycbiwdcbyiwdcuiwchwicwhco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.app = app
db.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(bookmarks)


