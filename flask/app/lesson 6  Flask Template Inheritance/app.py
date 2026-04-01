# ============================================================
# Lesson 6 - Template Inheritance
# File: app.py
# Purpose: Render pages that extend a common base template
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# Home page template (extends base.html)
@app.route("/")
def home():
    return render_template("home.html")

# About page template (also extends base.html)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)