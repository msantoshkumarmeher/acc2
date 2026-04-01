import sqlite3

# ============================================================
# Lesson 8 - Database Initialization Script
# File: templates/database.py
# Purpose: Create students table (manual setup script)
# Note: File location is unusual; normally this should be outside templates
# ============================================================

conn = sqlite3.connect("database.db")

# Create students table
conn.execute("""
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
""")

# Close DB connection
conn.close()