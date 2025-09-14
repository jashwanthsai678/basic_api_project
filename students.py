from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_FILE = "students_data.json"
API_KEY = "mysecretapikey"  # 🔑 Set your API key here

# Load or initialize data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
else:
    students = [
        {"id": 1, "name": "Alice", "grade": "A"},
        {"id": 2, "name": "Bob", "grade": "B"}
    ]
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

@app.route("/")
def home():
    return "🎉 Welcome to the Students API!"

@app.route("/students", methods=["GET", "POST"])
def handle_students():
    # ✅ Validate API key
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        abort(401, description="Unauthorized: Invalid API key")

    if request.method == "GET":
        return jsonify(students)

    if request.method == "POST":
        data = request.get_json()
        if not data or not data.get("name") or not data.get("grade"):
            return jsonify({"error": "Name and grade are required!"}), 400
        new_student = {
            "id": len(students) + 1,
            "name": data["name"],
            "grade": data["grade"]
        }
        students.append(new_student)
        with open(DATA_FILE, "w") as f:
            json.dump(students, f, indent=4)
        return jsonify({"message": "✅ Student added successfully!", "student": new_student}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)
