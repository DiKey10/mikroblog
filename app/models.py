# app/models.py
from datetime import datetime
from app import db

class Ksiazki(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   nazwa_ksiazki = db.Column(db.String(100), index=True, unique=True)
   autor = db.Column(db.String(200), index=True, unique=True)
   posts = db.relationship("Wypozyczenia", backref="nazwa_ksiazki", lazy="dynamic")

   def __str__(self):
       return f"<User {self.username}>"

class Wypo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   informacje_wypozyczenie = db.Column(db.Text)
   nazwa_ksiazki = db.Column(db.String(100), index=True, unique=True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   def __str__(self):
       return f"<Wypo {self.nazwa_ksiazki} {self.informacje_wypozyczenie[:50]} ...>"