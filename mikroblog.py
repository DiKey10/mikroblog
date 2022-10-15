# mikroblog.py

from app import app, db
from app.models import Ksiazki, Wypo

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Ksiazki": Ksiazki,
       "Wypo": Wypo
   }
