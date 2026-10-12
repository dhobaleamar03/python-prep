# Creating PUT and DELETE endpoints using Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

#store sample users in a dictionary
users = {
    1: {"id": 1, "name": "Pawan"},
    2: {"id": 2, "name": "Rahul"}
}

# update a user's name
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # check whether the user exists
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    # Read the updated data from the request
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    # Save the new name
    users[user_id]["name"] = data["name"]
    return jsonify(users[user_id]), 200


# delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Check whether the user exists
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    # Remove the user and return the deleted record
    deleted_user = users.pop(user_id)
    return jsonify(deleted_user), 200


#start the local development server
if __name__ == "__main__":
    app.run(debug=True)