import json
from flask import Flask, request
from db import db

# define db filename
db_filename = "todo.db"
app = Flask(__name__)

# setup config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# initialize app
db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

# your routes here

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/users/", methods=["POST"])
def create_user():
    # temporary response (Code below isn't correct implementation and just for
    # testing purposes)
    body = json.loads(request.data)
    username = body.get("username")
    password = body.get("password")
    if username is None or password is None:
        return failure_response("Username and password required")
    return success_response({"username": username, "password": password})

@app.route("/api/users/", methods=["GET"])
def get_users():
    # temporary response
    return success_response({"username": "John Doe", "password": "password"})






# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
  