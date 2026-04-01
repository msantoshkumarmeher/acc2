# ============================================================
# Lesson 3 - Static Files (CSS, JS, Images)
# File: app.py
# Purpose: Render a template that uses static assets
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# Home route renders index.html
# Static files are referenced inside template using url_for('static', ...)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)