from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "ali", "email": "ali@"},
    {"id": 2, "name": "abbas", "email": "abbas@"},
    {"id": 3, "name": "nikoo", "email": "nikoo@"}
]

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "user not found"})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
            "id": len(users),
            "username": data.get("name"),
            "age": data.get("age")
    }
    users.append(new_user)
    return jsonify(new_user)

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            user["age"] = data.get("age")
            return jsonify(user)
    return jsonify({"message": "user not found"}) , 404

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users.remove(user_id)

@app.route("/")
def home():
    return "welcome home page"

if __name__ == "__main__":
    app.run(debug=True)