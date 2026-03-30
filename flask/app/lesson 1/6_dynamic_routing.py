from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is home Page</h1>"

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello {name} </h1>"

if __name__ == "__main__":
    app.run(debug=True)