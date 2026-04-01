from flask import Flask, render_template, request

# ============================================================
# Lesson 4 - POST Method
# File: app.py
# Purpose: Receive form data sent using HTTP POST
# ============================================================

app = Flask(__name__)

# Show form page
@app.route("/")
def home():
    return render_template("form.html")

# Handle submitted form data (POST request)
@app.route("/submit", methods=["POST"])
def submit():
    # request.form reads form fields by their input name
    name = request.form["username"]
    age = request.form["age"]

    # Return simple text response
    return f"Name: {name}, Age: {age}"

# @app.route("/submit", methods=["POST"])
# def submit():

#     name = request.form["username"]
#     age = request.form["age"]

#     return render_template("result.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)