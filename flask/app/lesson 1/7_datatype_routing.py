from flask import Flask

# ============================================================
# Lesson 1 - Datatype Converter in Routes
# File: 7_datatype_routing.py
# Purpose: Restrict dynamic URL values to specific data types
# ============================================================

app = Flask(__name__)

# <int:id> means this route will match only integer values
# Example works:   /student/101
# Example fails:   /student/abc
@app.route("/student/<int:id>")
def student(id):
    return f"Student ID is {id}"

if __name__ == "__main__":
    app.run(debug=True)


# Common Flask route converters:
# | Converter | Example        | Description                        |
# |-----------|----------------|------------------------------------|
# | string    | <name>         | default text type                  |
# | int       | <int:id>       | integers only                      |
# | float     | <float:price>  | decimal numbers                    |
# | path      | <path:file>    | accepts slashes in the value       |
# | uuid      | <uuid:id>      | UUID values                        |
