from flask import Flask, render_template

# ============================================================
# Basic Flask App Example
# File: APP/app.py
# Purpose: Render a simple home page template
# ============================================================

app = Flask(__name__)


@app.route('/')
def home():
    # Render home.html from templates folder
    return render_template('home.html') 

if __name__ == '__main__':
    # Run app in debug mode for development
    app.run(debug=True)