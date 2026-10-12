from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON object required"}), 400

    name = data.get("name")
    age = data.get("age")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Valid name is required"}), 400

    if type(age) is not int or age < 0:
        return jsonify({"error": "Age must be a non-negative integer"}), 400

    return jsonify({
        "name": name.strip(),
        "age": age
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
    