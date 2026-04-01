# ============================================================
# Lesson 1 - Multiple Routes Example
# File: 4_example.py
# Purpose: Show how to define multiple URL routes in Flask
# ============================================================

from flask import Flask

app = Flask(__name__)

# Route for /hello → returns a greeting
# Visit: http://127.0.0.1:8000/hello
@app.route("/hello")
def hello():
    return "Hello Students!"

# Route for /about → returns a description
# Visit: http://127.0.0.1:8000/about
@app.route("/about")
def about():
    return "This is Flask Tutorial"

# port=8000 changes the default port from 5000 to 8000
if __name__ == "__main__":
    app.run(debug=True, port=8000)