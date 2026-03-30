# import os
# import sqlite3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(BASE_DIR, "database.db")

# print("cwd=", os.getcwd())
# print("Using database path:", DB_PATH)

# try:
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       name TEXT NOT NULL,
#       age INTEGER,
#       course TEXT
#     )
#     """)

#     conn.commit()
#     print("Database and table created/verified successfully")
# except Exception as e:
#     print("Error creating database/table:", e)
# finally:
#     if 'conn' in locals():
#         conn.close()

import os
import sqlite3

# Same database path logic (important!)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Data to insert (5 records)
    students_data = [
        ("Santosh", 25, "Computer Science"),
        ("Ravi", 22, "Mechanical"),
        ("Priya", 23, "Electrical"),
        ("Anjali", 24, "Civil"),
        ("Rahul", 21, "Information Technology")
    ]

    # Insert multiple records
    cursor.executemany(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        students_data
    )

    conn.commit()
    print("5 records inserted successfully")

except Exception as e:
    print("Error inserting data:", e)

finally:
    if 'conn' in locals():
        conn.close()