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



################## Loop Example ##################################################

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/students")
def students():
    student_list = ["Rahul", "Amit", "Priya"]
    return render_template("students.html", students=student_list)

if __name__ == "__main__":
    app.run(debug=True)
