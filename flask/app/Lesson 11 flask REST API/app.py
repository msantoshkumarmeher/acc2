from flask import Flask, request, jsonify
import sqlite3
import os

# ============================================================
# Lesson 11 - Flask REST API
# File: app.py
# Purpose: Build CRUD API endpoints for student data
# ============================================================

app = Flask(__name__)

# -----------------------------
# Database Configuration
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_db():
    # Open DB connection and return rows as dictionary-like objects
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# Initialize Database
# -----------------------------
def init_db():
    # Create students table once when app starts
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()


init_db()


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Flask REST API is running",
        "endpoints": {
            "GET all": "/api/students",
            "GET one": "/api/student/<id>",
            "POST": "/api/add",
            "PUT": "/api/update/<id>",
            "DELETE": "/api/delete/<id>"
        }
    })


# -----------------------------
# GET All Students
# -----------------------------
@app.route("/api/students", methods=["GET"])
def get_students():
    # Fetch all students
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    result = []
    for s in students:
        # Convert each DB row to JSON-ready dictionary
        result.append({
            "id": s["id"],
            "name": s["name"],
            "age": s["age"]
        })

    return jsonify({
        "status": "success",
        "count": len(result),
        "students": result
    })


# -----------------------------
# GET Single Student
# -----------------------------
@app.route("/api/student/<int:id>", methods=["GET"])
def get_student(id):
    # Fetch one student by id
    conn = get_db()
    s = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()
    conn.close()

    if s:
        return jsonify({
            "status": "success",
            "data": {
                "id": s["id"],
                "name": s["name"],
                "age": s["age"]
            }
        })

    return jsonify({
        "status": "error",
        "message": "Student not found"
    }), 404


# -----------------------------
# ADD Student (POST)
# -----------------------------
@app.route("/api/add", methods=["POST"])
def add_student():
    # Parse JSON request body
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({
            "status": "error",
            "message": "Invalid data"
        }), 400

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (data["name"], data["age"])
    )
    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Student added successfully"
    }), 201


# -----------------------------
# UPDATE Student (PUT)
# -----------------------------
@app.route("/api/update/<int:id>", methods=["PUT"])
def update_student(id):
    # Parse JSON request body for updated values
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({
            "status": "error",
            "message": "Invalid data"
        }), 400

    conn = get_db()
    cursor = conn.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (data["name"], data["age"], id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({
            "status": "error",
            "message": "Student not found"
        }), 404

    conn.close()

    return jsonify({
        "status": "success",
        "message": "Student updated successfully"
    })


# -----------------------------
# DELETE Student
# -----------------------------
@app.route("/api/delete/<int:id>", methods=["DELETE"])
def delete_student(id):
    # Delete student by id
    conn = get_db()
    cursor = conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({
            "status": "error",
            "message": "Student not found"
        }), 404

    conn.close()

    return jsonify({
        "status": "success",
        "message": "Student deleted successfully"
    })


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)