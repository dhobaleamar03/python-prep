# Creating a POST endpoint to receive user data

from flask import Flask, jsonify, request

app = Flask(__name__)

# Accept a new user at the /users endpoint
@app.route("/users", methods=["POST"])
def create_user():
    # Read the JSON data sent by the client
    data = request.get_json()

    # check whether the name was provided
    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    # Prepare the response using the submitted name
    user = {
        "id": 1,
        "name": data["name"]
    }

    # return 201 to indicate successful creation
    return jsonify(user), 201

# start the local development server
if __name__ == "__main__":
    app.run(debug=True)