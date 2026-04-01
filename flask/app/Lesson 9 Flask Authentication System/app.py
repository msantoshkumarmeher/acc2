from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3

# ============================================================
# Lesson 9 - Basic Authentication System
# File: app.py
# Purpose: Register, login, dashboard access, logout using sessions
# ============================================================

app = Flask(__name__)
# Secret key is required for session management
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# Open DB connection and return rows like dictionaries
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# Home → Redirect to login
@app.route("/")
def home():
    return redirect(url_for("login"))


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # Collect registration form data
        username = request.form["username"]
        password = request.form["password"]

        # Save user credentials to DB
        # Note: Plain text passwords are for learning only (not secure in production)
        conn = get_db()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Read login form inputs
        username = request.form["username"]
        password = request.form["password"]

        # Check if matching user exists
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            # Store logged-in user in session
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    # Allow access only when user is logged in
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # Remove user from session (log out)
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)