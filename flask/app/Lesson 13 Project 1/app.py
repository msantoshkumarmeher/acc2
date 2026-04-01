from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os

# ============================================================
# Lesson 13 - Mini Project (Auth + Student CRUD + API)
# File: app.py
# Purpose: Combine login system and student management in one app
# ============================================================

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-me")

DB = "database.db"

# Open DB connection and return rows as dictionary-like objects
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


# ----------------- INIT DB -----------------
def init_db():
    # Create users table
    conn = get_db()
    # Create students table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()
    conn.close()

init_db()


# ----------------- AUTH -----------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Read login form values
        u = request.form["username"]
        p = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u, p)
        ).fetchone()
        conn.close()

        if user:
            # Save login state in session
            session["user"] = u
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Read registration form values
        u = request.form["username"]
        p = request.form["password"]

        conn = get_db()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (u, p)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ----------------- DASHBOARD -----------------

@app.route("/dashboard")
def dashboard():
    # Only logged-in users can access dashboard
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# ----------------- STUDENT CRUD -----------------

@app.route("/students")
def students():
    # Fetch all student records for listing
    conn = get_db()
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("students.html", students=data)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Read form data and insert student
        name = request.form["name"]
        age = request.form["age"]

        conn = get_db()
        conn.execute(
            "INSERT INTO students (name, age) VALUES (?, ?)",
            (name, age)
        )
        conn.commit()
        conn.close()

        return redirect("/students")

    return render_template("add_student.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        # Read updated form values
        name = request.form["name"]
        age = request.form["age"]

        conn.execute(
            "UPDATE students SET name=?, age=? WHERE id=?",
            (name, age, id)
        )
        conn.commit()
        conn.close()
        return redirect("/students")

    student = conn.execute(
        "SELECT * FROM students WHERE id=?", (id,)
    ).fetchone()

    conn.close()
    return render_template("edit_student.html", student=student)


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/students")


# ----------------- API -----------------

@app.route("/api/students")
def api_students():
    # JSON endpoint for all students
    conn = get_db()
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    result = []
    for s in data:
        result.append(dict(s))

    return jsonify(result)


# ----------------- RUN -----------------

if __name__ == "__main__":
    app.run(debug=True)