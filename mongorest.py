
from flask import Flask
from flask_restx import Api, Resource, fields
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBName'] = 'stars'
# Change the MONGO_URI with provided connection String in Canvas
app.config['MONGO_URI'] = 'mongodb+srv://ift101:AY3qamqzeI4rHOBn@cluster0.qw7goz5.mongodb.net/restdb?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.stars
    output = []
    for s in star.find():
        output.append({'name': s['name'],
                      'distance': s['distance']})
    return jsonify({'result': output})


@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result': output})




def get_connection(self):
    try:
        client = MongoClient(MongoDbConnection.CONNECTION_STR)
        db = client.restdb
        return db
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)
