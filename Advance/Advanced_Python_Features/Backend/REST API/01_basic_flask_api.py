#Creating a basic API using Flask

from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)

# define the home endpoint
@app.route("/")
def home():
    #return the response as JSON
    return jsonify({"message": "Welcome to my API!"})

# Start the server when this file runs directly
if __name__ == "__main__":
    app.run(debug=True)