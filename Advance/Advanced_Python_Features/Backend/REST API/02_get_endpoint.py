# Creating a GET endpoint to return users
from flask import Flask, jsonify

app = Flask(__name__)

# sample user data
users = [
    {"id": 1, "name": "Pawan"},
    {"id": 2, "name": "Rahul"}
]

#return the list when someone requests /users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# start the local development server
if __name__ == "__main__":
    app.run(debug=True)