from flask import Flask

app = Flask(__name__)

@app.route("/product/<name>/<int:price>")
def product(name, price):
    return f"Product: {name}, Price: {price}"

if __name__ == "__main__":
    app.run(debug=True)