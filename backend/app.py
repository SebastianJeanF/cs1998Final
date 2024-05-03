import json
from flask import Flask, request
from db import db, User, Card, Deck, Class 
from flask_sqlalchemy import SQLAlchemy

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
    Class.create_hardcoded_classes()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

# your routes here

@app.route("/")
def hello_world():
    return "Hello, World!"


"""
Route to create the user. Returns error code 400 if no usernmae or password provided in 
request body, otherwise makes the new User, commits it to the database, and
returns a 201 success code along with the serialization.
"""
@app.route("/api/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    username = body['username']
    #these checks are in case front-end doesn't handle clicking without filling a field.
    if username is None:
        return failure_response("No username provided", 400)
    password = body['password']
    if password is None:
        return failure_response("No password provided", 400)
    
    new_user = User(username=username, password=password) #create new Course object with given code and name
    db.session.add(new_user) #add object to sqlAlchemy session and commit to database. This is effectively one row in courses table
    db.session.commit()
    return success_response(new_user.serialize(), 201)

"""
Returns serialization all users in User
"""
@app.route("/api/users/")
def get_users():
    #note query.all() returns every value in this query as a list. 
    users = [c.serialize() for c in User.query.all()] 
    return success_response(users)


"""
Check if user with provided username and password exists. If does, then returns serialized form in success response 200, else "no such user" message with 400 code.
"""
@app.route("/api/users/")
def get_spec_user():
    #assuming the data is being passed in through login fields
    body = json.loads(request.data)
    username = body['username']
    #these checks are in case front-end doesn't handle clicking without filling a field.
    if username is None:
        return failure_response("No username provided", 400)
    password = body['password']
    if password is None:
        return failure_response("No password provided", 400)
    user_val = User.query.filter(User.username==username, User.password==password).first()
    if user_val is None:
        return failure_response("false", 400)
    else:
        return success_response("true", 200)

"""
Returns serialization all classes in Class. Note this will return the information of 3 classes of CS 2110, CS 3110, and CS 1998 due to hard-code function
but additionally associated deck information
"""
@app.route("/api/users/<int:user_id>/classes/")
def get_classes():
    #note query.all() returns every value in this query as a list. 
    classes = [c.serialize() for c in Class.query.all()] 
    return success_response(classes)


"""
Returns serialization of all decks in a class that are either public or private and created by the logged-in user.
"""
@app.route("/api/users/<int:user_id>/classes/<int:class_id>/decks")
def get_rel_decks(user_id, class_id):
    desired_class = Class.query.get(class_id) #note 0, 1, and 2 class id numbering
    if desired_class is None:
        return failure_response("No such class", 400)
    
    #First condition -- decks must be associated with the class. Second condition -- deck is either public, or it is private and associated with the user_id.
    #Note use of & and | needed since SQL uses bitwise operators
    filter_decks = Deck.query.filter(
        (Deck.class_id == class_id) &
        ((Deck.is_public == True) | ((Deck.is_public == False) & (Deck.user_id == user_id)))
    ).all()

    serialized_rel_decks = [c.serialize() for c in filter_decks]
    return success_response(serialized_rel_decks)







# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
  