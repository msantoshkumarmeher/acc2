import sqlite3

# ============================================================
# Lesson 9 - Users Table Setup
# File: database.py
# Purpose: Create users table for authentication example
# ============================================================

conn = sqlite3.connect("database.db")

# Create users table if it does not already exist
conn.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

# Close DB connection
conn.close()