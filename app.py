"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, redirect, flash, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

app.app_context().push()
connect_db(app)

# *route for homepage

@app.route('/')
def homepage():
    """Shows homepage"""
    
    cupcakes = Cupcake.query.all()
    
    return render_template('index.html', cupcakes=cupcakes)

# *api route for cupcakes
# TODO all api routes must be jsonified in some way
# get all cupcakes
@app.route('/api/cupcakes')
def show_all_cupcakes():
    """Shows all cupcakes in database.
    """
    # *serialize cupcakes
    # call for each cupcake serialize method for each cupcake in database by querying all cupcakes
    cupcakes_serialized = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes_serialized)

# get cupcake by id
@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_by_id(cupcake_id):
    """Shows a cupcake by id.
    """
    # *serialize cupcake
    # call for cupcake serialize method for cupcake by querying cupcake by id
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

# post cupcake
@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Makes a post request to create a new cupcake and submits it to the api.
    """
    # *create new instane of cupcake and a seriazlized instance for the api
    print(request.json)
    new_cupcake = Cupcake(
        flavor = request.json["flavor"],
        size = request.json["size"],
        rating = request.json["rating"],
        image = request.json["image"]
    )
    print(request.json)
    # *save new cupcake to the database
    db.session.add(new_cupcake)
    db.session.commit()
    
    # *return response in json
    response_json = jsonify(cupcake=new_cupcake.serialize())
    
    return (response_json, 201)

# patch cupcake
@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake_by_id(cupcake_id):
    """Updates a cupcate in the database based off of it's id.

    Args:
        cupcake_id (int): cupcake_id
        
    Return:
        A cupcake from the database based off the id that was queried.
    """
    # *Query the cupcake, update by it's keys and save to database
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    
    db.session.commit()
    
    return jsonify(cupcake=cupcake.serialize())  
           
# delete cupcake
@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake_by_id(cupcake_id):
    """Deletes a cupcake from the database based off of it's ud

    Args:
        cupcake_id (int): cupcake_id

    Returns:
        string: JSON message of deleted.
    """
    # *Query, delete, save
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="deleted")