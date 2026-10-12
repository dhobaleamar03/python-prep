# Validating requests and returning HTTP status codes

from flask import Flask, jsonify, request
app = Flask(__name__)

# accept a new user through a POST request
@app.route("/users", methods=["POST"])
def create_user():
    #rread JSON without raising an error for invalid JSON
    data = request.get_json(silent=True)

    # check whether valid JSON data was provided
    if not data:
        return jsonify({"error": "Valid JSON is required"}), 400

    # Get the user's name from the request
    name = data.get("name")

    #check that the name is a non-empty string
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "A valid name is required"}), 400

    # prepare the user response
    user = {"id": 1, "name": name.strip()}

    # return 201 when the user is created successfully
    return jsonify(user), 201


#start the local development server
if __name__ == "__main__":
    app.run(debug=True)