# ============================================================
# Lesson 1 - Dynamic Routing
# File: 6_dynamic_routing.py
# Purpose: Show how to capture values from the URL
# ============================================================

from flask import Flask

app = Flask(__name__)

# Static route — URL is always the same
@app.route("/")
def home():
    return "<h1>This is home Page</h1>"

# Dynamic route — <name> is a variable part of the URL
# Example: visiting /user/Santosh will pass "Santosh" as the name argument
# Try: http://127.0.0.1:5000/user/Santosh
@app.route("/user/<name>")
def user(name):
    # The captured value is available as a function parameter
    return f"<h1>Hello {name} </h1>"

if __name__ == "__main__":
    app.run(debug=True)