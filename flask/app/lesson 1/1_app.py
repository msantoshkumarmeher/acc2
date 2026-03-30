from flask import Flask  #Imports the Flask class.

app = Flask(__name__)   #Creates a Flask application object.

@app.route("/")  #This defines a URL route. 
def home():
    return "Hello, Welcome to Flask!"

if __name__ == "__main__":
    app.run(debug=True)