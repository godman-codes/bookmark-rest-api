from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import string
import random

db = SQLAlchemy()

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable = False)
   email = db.Column(db.String(120), unique=True, nullable = False)
   password = db.Column(db.Text, nullable = False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   bookmarks = db.relationship('Bookmarks', backref='user')

   def __repr__(self) -> str:
      return 'User>>> {self.username}'

class Bookmarks(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   body = db.Column(db.Text, nullable=True)
   url = db.Column(db.Text, nullable=False)
   short_url = db.Column(db.String(3), nullable=True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   visits = db.Column(db.Integer, default=0)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())

   def generate_short_character(self):
      characters = string.digits+string.ascii_letters
      picked_chars = ''.join(random.choices(characters, k=3))

      link=self.query.filter_by(short_url=picked_chars).first()

      if link:
         self.generate_short_character()
      else:
         return picked_chars

   def __init__(self, **kwargs):
      super().__init__(**kwargs)

      self.short_url = self.generate_short_character()

   def __repr__(self) -> str:
      return 'Bookmarks>>> {self.url}'