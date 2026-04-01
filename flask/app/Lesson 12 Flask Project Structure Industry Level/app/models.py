from app.database import get_db

# ============================================================
# Lesson 12 - Model/DB Helper Functions
# File: app/models.py
# Purpose: Keep SQL operations separate from route handlers
# ============================================================

# Create Table
def init_db():
    # Create students table if not present
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    db.commit()


# CRUD FUNCTIONS

def get_all_students():
    # Return all student records
    db = get_db()
    return db.execute("SELECT * FROM students").fetchall()


def get_student(id):
    # Return one student by id
    db = get_db()
    return db.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()


def add_student(name, age):
    # Insert new student record
    db = get_db()
    db.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )
    db.commit()


def update_student(id, name, age):
    # Update existing student record
    db = get_db()
    db.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (name, age, id)
    )
    db.commit()


def delete_student(id):
    # Delete student record by id
    db = get_db()
    db.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )
    db.commit()