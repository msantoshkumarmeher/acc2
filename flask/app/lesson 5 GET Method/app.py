from flask import Flask, render_template, request

# ============================================================
# Lesson 5 - GET Method
# File: app.py
# Purpose: Receive form data sent using HTTP GET (query string)
# ============================================================

app = Flask(__name__)

# Show form page
@app.route("/")
def home():
    return render_template("form.html")

# Handle form submission through GET
@app.route("/submit", methods=["GET"])
def submit():
    # request.args reads values from URL query parameters
    # Example URL: /submit?username=Rahul&age=22
    name = request.args.get("username")
    age = request.args.get("age")

    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    app.run(debug=True)