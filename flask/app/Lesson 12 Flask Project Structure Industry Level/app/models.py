from app.database import get_db

# Create Table
def init_db():
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
    db = get_db()
    return db.execute("SELECT * FROM students").fetchall()


def get_student(id):
    db = get_db()
    return db.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()


def add_student(name, age):
    db = get_db()
    db.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )
    db.commit()


def update_student(id, name, age):
    db = get_db()
    db.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (name, age, id)
    )
    db.commit()


def delete_student(id):
    db = get_db()
    db.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )
    db.commit()