from flask import Flask
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ege:ege123@cluster0.smbge.gcp.mongodb.net/testdb?retryWrites=true&w=majority")

db = cluster['testdb']
collection = db["testcol"]

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
    
        post1 = {"_id": 999, "name": "deneme", "score":9999999}
        
        collection.insert_one(post1)
    
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)