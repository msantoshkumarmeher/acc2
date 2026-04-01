from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

# ============================================================
# Lesson 8 - CRUD Operations with Flask + SQLite
# File: app.py
# Purpose: Create, read, update, delete student records
# ============================================================

app = Flask(__name__)

# Database file location
DB_PATH = os.path.join(app.root_path, "database.db")

# Open a DB connection and return rows like dictionaries
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Create table if it does not exist
def init_db():
    os.makedirs(app.root_path, exist_ok=True)
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

@app.route("/")
def index():
    # Read all students for listing page
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        # Read form values
        name = request.form["name"]
        age = request.form["age"]

        # Insert new record
        conn = get_db()
        conn.execute(
            "INSERT INTO students (name, age) VALUES (?, ?)",
            (name, age)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = get_db()

    if request.method == "POST":
        # Read updated values from form
        name = request.form["name"]
        age = request.form["age"]

        conn.execute(
            "UPDATE students SET name=?, age=? WHERE id=?",
            (name, age, id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return redirect(url_for("index"))

    return render_template("edit.html", student=student)


@app.route("/delete/<int:id>")
def delete(id):

    # Delete selected student by id
    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    # Ensure DB/table exists before app starts
    with app.app_context():
        init_db()
    app.run(debug=True)