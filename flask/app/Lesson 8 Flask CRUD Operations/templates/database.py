import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
""")

conn.close()