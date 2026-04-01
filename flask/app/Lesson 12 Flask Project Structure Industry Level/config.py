import os


class Config:
    # Secret key used for sessions and security-related features
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-me")
    # SQLite database file name
    DATABASE = "database.db"