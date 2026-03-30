from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

app = Flask(__name__)

DB_PATH = os.path.join(app.root_path, "database.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

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
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

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

    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)