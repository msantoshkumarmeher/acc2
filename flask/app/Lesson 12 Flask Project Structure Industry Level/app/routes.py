from flask import Blueprint, request, jsonify
from app.models import *

bp = Blueprint("routes", __name__)

# Home
@bp.route("/")
def home():
    return {"message": "Flask Structured API"}


# GET all
@bp.route("/students", methods=["GET"])
def students():
    data = get_all_students()

    result = []
    for s in data:
        result.append({
            "id": s["id"],
            "name": s["name"],
            "age": s["age"]
        })

    return jsonify(result)


# POST
@bp.route("/add", methods=["POST"])
def add():
    data = request.json
    add_student(data["name"], data["age"])
    return {"message": "Student added"}


# PUT
@bp.route("/update/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    update_student(id, data["name"], data["age"])
    return {"message": "Updated"}


# DELETE
@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    delete_student(id)
    return {"message": "Deleted"}