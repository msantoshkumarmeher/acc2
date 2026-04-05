from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Santosh"},
    {"id": 2, "name": "Rahul"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return {"message": "Student not found"}



@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return {"message": "Student added successfully"}

@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            return {"message": "Updated successfully"}
    return {"message": "Student not found"}


@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message": "Deleted successfully"}
    return {"message": "Student not found"}

if __name__ == '__main__':
    app.run(debug=True)