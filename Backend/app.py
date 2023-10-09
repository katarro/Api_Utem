from database.db_config import init_app as init_db
from flask import Flask, jsonify, request
from models.resource import Resource, db
from flask_cors import CORS
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
CORS(app)

@app.route('/api/resource/', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([resource.serialize() for resource in resources])

@app.route('/api/resource/<int:id>', methods=['GET'])
def get_resource_by_id(id):
    resource = Resource.query.get(id)
    if resource:
        return jsonify(resource.serialize())
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route('/api/resource/', methods=['POST'])
def post_resource():
    required_fields = ["contact_number", "first_name", "item_description", "item_image", "last_name", "sede"]
    if not all(field in request.json for field in required_fields):
        return jsonify({"message": "Bad request, missing fields"}), 400

    new_resource = Resource(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        contact_number=request.json['contact_number'],
        sede=request.json['sede'],
        item_image=request.json['item_image'],
        item_description=request.json['item_description']
    )
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(new_resource.serialize()), 201

@app.route('/api/resource/<int:id>', methods=['PUT'])
def put_resource(id):
    resource = Resource.query.get(id)
    if not resource:
        return jsonify({"message": "Item not found"}), 404

    for key, value in request.json.items():
        setattr(resource, key, value)
    db.session.commit()
    return jsonify(resource.serialize())

@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    resource = Resource.query.get(id)
    if not resource:
        return jsonify({"message": "Item not found"}), 404

    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
