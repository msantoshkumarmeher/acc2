from flask import Blueprint, request, jsonify
from app.models import *


# Blueprint groups all route handlers in this module
bp = Blueprint("routes", __name__)

# Home
@bp.route("/")
def home():
    return {"message": "Flask Structured API"}


# GET all
@bp.route("/students", methods=["GET"])
def students():
    # Read all students from model function
    data = get_all_students()

    result = []
    for s in data:
        # Convert row object to JSON-friendly dictionary
        result.append({
            "id": s["id"],
            "name": s["name"],
            "age": s["age"]
        })

    return jsonify(result)


# POST
@bp.route("/add", methods=["POST"])
def add():
    # Read JSON body and create student
    data = request.json
    add_student(data["name"], data["age"])
    return {"message": "Student added"}


# PUT
@bp.route("/update/<int:id>", methods=["PUT"])
def update(id):
    # Read JSON body and update selected student
    data = request.json
    update_student(id, data["name"], data["age"])
    return {"message": "Updated"}


# DELETE
@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    # Delete selected student
    delete_student(id)
    return {"message": "Deleted"}