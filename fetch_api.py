from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

SOURCE_API = "http://127.0.0.1:5000/students"
API_KEY = "mysecretapikey"  # 🔑 Must match students.py

@app.route("/")
def home():
    return fetch_students()

@app.route("/fetch_students")
def fetch_students():
    try:
        response = requests.get(SOURCE_API, headers={"x-api-key": API_KEY})
        response.raise_for_status()
        data = response.json()
        return render_template("students.html", students=data)
    except Exception as e:
        return f"❌ Failed to fetch data: {e}", 500

@app.route("/search_students")
def search_students():
    query = request.args.get("q", "").lower()
    try:
        response = requests.get(SOURCE_API, headers={"x-api-key": API_KEY})
        response.raise_for_status()
        students = response.json()
        filtered = [s for s in students if query in s.get("name", "").lower()]
        return jsonify(filtered)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
