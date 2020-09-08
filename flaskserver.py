from flask import Flask
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
import random

cluster = MongoClient("mongodb+srv://ege:ege123@cluster0.smbge.gcp.mongodb.net/testdb?retryWrites=true&w=majority")

db = cluster['office']
collection = db["reservations"]

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource): ### Sample class
    def get(self):
        
        #post1 = {"name": "deneme", "score":9999999}        
        #collection.insert_one(post1)
    
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class reserve(Resource): # Make reservation class
    def get(self,month,day, hour,name):
    
        db = cluster['office']
        collection = db["reservations"]
        
        result_list =[]
        results = collection.find({"month": month, "day":day, "hour":hour, "room":name})
        
        for result in results:
            result_list.append(result)
            print(result)
        if len(result_list) == 0: ### Checks if room is occupied
            post1 = {"month": month, "day":day, "hour":hour, "room":name}        
            collection.insert_one(post1)    
            return {'succesful': 'reservation'}
        else:
            return {'room': 'occupied'}


api.add_resource(reserve, '/reserve/<string:month>/<string:day>/<string:hour>/<string:name>')

class deleteres(Resource): ### Reservation delete class
    def get(self,month,day, hour,name):
    
        db = cluster['office']
        collection = db["reservations"]
        
        result_list =[]
        results = collection.find({"month": month, "day":day, "hour":hour, "room":name})
        #print(results.length())
        for result in results:
            result_list.append(result)
            print(result)
        if len(result_list) == 0: # Checks if reservatiom exists       
            return {'no': 'res'}
        else:
            myquery = { "month": month, "day":day, "hour":hour, "room":name }
            collection.delete_one(myquery)
            return {'res': 'deleted'}


api.add_resource(deleteres, '/deleteres/<string:month>/<string:day>/<string:hour>/<string:name>')


class changeprice(Resource):  #Change price of a room
    def get(self,month,day, hour,name):
    
        db = cluster['office']
        collection = db["rooms"]
        
        result_list =[]
        results = collection.find({"name": room})
        #print(results.length())
        for result in results:
            result_list.append(result)
            print(result)
        if len(result_list) == 0:            
            return {'no': 'room'}
        else:
            myquery = { "name": room }
            newvalues = { "$set": { "price": price } }
            collection.delete_one(myquery)
            return {'res': 'deleted'}


api.add_resource(changeprice, '/changeprice/<string:room>/<string:price>')




if __name__ == '__main__':
    app.run(debug=True)