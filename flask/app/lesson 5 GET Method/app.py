from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["GET"])
def submit():

    name = request.args.get("username")
    age = request.args.get("age")

    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    app.run(debug=True)