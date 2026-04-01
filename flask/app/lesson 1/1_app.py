# ============================================================
# Lesson 1 - Introduction to Flask
# File: 1_app.py
# Purpose: Your very first Flask web application
# ============================================================

# Import the Flask class from the flask library
# Flask is a lightweight web framework for Python
from flask import Flask

# Create a Flask application instance
# __name__ tells Flask where to look for resources (templates, static files, etc.)
app = Flask(__name__)

# Define a route — this maps a URL to a Python function
# "/" means the home page (e.g., http://127.0.0.1:5000/)
@app.route("/")
def home():
    # Whatever you return here is shown in the browser
    return "Hello, Welcome to Flask!"

# Run the app only when this file is executed directly (not imported)
# debug=True enables auto-reload and shows error messages in the browser
if __name__ == "__main__":
    app.run(debug=True)