# This is a temporary editor-generated file and appears incomplete/corrupted.
# It is not required for the lesson app to work.
, render_template

app = Flask(__name__)

@app.route("/students")
def students():
    student_list = ["Rahul", "Amit", "Priya"]
    return render_template("students.html", students=student_list)

if __name__ == "__main__":
    app.run(debug=True)
