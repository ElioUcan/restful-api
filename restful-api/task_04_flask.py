#!/usr/bin/python3
"""Flask API implementation for task 04."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Home address returning welcome string."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return json data with usernames list."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return full user object or 404 if not found."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
