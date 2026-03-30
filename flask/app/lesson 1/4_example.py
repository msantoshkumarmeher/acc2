from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello Students!"

@app.route("/about")
def about():
    return "This is Flask Tutorial"

if __name__ == "__main__":
    app.run(debug=True,port=8000)