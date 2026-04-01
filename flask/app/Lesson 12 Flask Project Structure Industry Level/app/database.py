import sqlite3
from flask import g
from config import Config

# Get one DB connection per request and store it in Flask `g`
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(Config.DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

# Close DB connection at request end
def close_db(e=None):
    db = g.pop("db", None)
    if db:
        db.close()