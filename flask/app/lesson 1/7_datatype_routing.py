from flask import Flask

app = Flask(__name__)

@app.route("/student/<int:id>")
def student(id):
    return f"Student ID is {id}"

if __name__ == "__main__":
    app.run(debug=True)


# | Converter | Example         | Description     |
# | --------- | --------------- | --------------- |
# | string    |  <name>         | default text    |
# | int       |  <int:id>       | integers only   |
# | float     |  <float:price>  | decimal numbers |
# | path      |  <path:file>    | accepts slashes |
# | uuid      |  <uuid:id>      | UUID values     |
