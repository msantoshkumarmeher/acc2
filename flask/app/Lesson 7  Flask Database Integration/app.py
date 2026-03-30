from flask import Flask, render_template, abort
import os
import sqlite3

app = Flask(__name__)

def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "database.db")


@app.route("/")
def home():
    return "Welcome to Flask Database Example"


@app.route("/students")
def students():
    db_path = get_db_path()

    if not os.path.exists(db_path):
        return "Database does not exist. Run create_db.py first.", 500

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()

    except sqlite3.OperationalError as e:
        return f"Database query error: {e}", 500

    finally:
        if 'conn' in locals():
            conn.close()

    return render_template("students.html", students=data)


if __name__ == "__main__":
    app.run(debug=True)