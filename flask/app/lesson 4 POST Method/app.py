from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["username"]
    age = request.form["age"]

    return f"Name: {name}, Age: {age}"

# @app.route("/submit", methods=["POST"])
# def submit():

#     name = request.form["username"]
#     age = request.form["age"]

#     return render_template("result.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)