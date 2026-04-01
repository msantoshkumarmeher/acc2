############ Render HTML Template #############

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)



################# Passing Data From Flask to HTML #################
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("passing_data.html", name="Santosh")

# if __name__ == "__main__":
#     app.run(debug=True)



# ============================================================
# Lesson 2 - Rendering Templates and Passing Data
# File: app.py
# Active Section: Loop Example
# Purpose: Send a Python list to HTML and render it using Jinja loop
# ============================================================

################## Loop Example ##################################################

from flask import Flask, render_template

app = Flask(__name__)

# Route to display student names using an HTML template
@app.route("/students")
def students():
    # Data prepared in Python
    student_list = ["Rahul", "Amit", "Priya"]
    # Pass data to template as variable `students`
    return render_template("students.html", students=student_list)

if __name__ == "__main__":
    app.run(debug=True)
