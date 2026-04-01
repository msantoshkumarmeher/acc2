# ============================================================
# Lesson 1 - Multiple URLs for One Function
# File: 5_multi_routes.py
# Purpose: Show how two different URLs can point to the same function
# ============================================================

from flask import Flask

app = Flask(__name__)

# Both "/" and "/home/" will call the same home() function
# This is useful when you want multiple URLs to show the same page
@app.route("/")
@app.route("/home/")
def home():
    return "Welcome to Flask"

if __name__ == "__main__":
    app.run(debug=True)