from flask import Flask
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
import random
from models import reservations


cluster = MongoClient("mongodb+srv://ege:ege123@cluster0.smbge.gcp.mongodb.net/testdb?retryWrites=true&w=majority")

db = cluster['office']
collection = db["reservations"]

app = Flask(__name__)
api = Api(app)
# reservation=reservations.Reservation(reservation_type="ege",reservation_dates="12.12.12").save()


class HelloWorld(Resource):
    def get(self):
        
        post1 = {"name": "deneme", "score":9999999}
        
        collection.insert_one(post1)
    
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class reserve(Resource):
    def get(self,month,day, hour,name):
        
        result_list =[]
        results = collection.find({"month": month, "day":day, "hour":hour, "room":name})
        #print(results.length())
        for result in results:
            result_list.append(result)
            print(result)
        if len(result_list) == 0:
            post1 = {"month": month, "day":day, "hour":hour, "room":name}        
            collection.insert_one(post1)    
            return {'succesful': 'world'}
        else:
            return {'room': 'occupied'}

#api.add_resource(HelloWorld, '/')
api.add_resource(reserve, '/reserve/<string:month>/<string:day>/<string:hour>/<string:name>')

class deleteres(Resource):
    def get(self,month,day, hour,name):
        
        result_list =[]
        results = collection.find({"month": month, "day":day, "hour":hour, "room":name})
        #print(results.length())
        for result in results:
            result_list.append(result)
            print(result)
        if len(result_list) == 0:            
            return {'no': 'res'}
        else:
            myquery = { "month": month, "day":day, "hour":hour, "room":name }
            collection.delete_one(myquery)
            return {'res': 'deleted'}

#api.add_resource(HelloWorld, '/')
api.add_resource(deleteres, '/deleteres/<string:month>/<string:day>/<string:hour>/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)




#### Model ####
from mongoengine import *
from datetime import datetime
from datetime import date
import json
import os

connect("test",host='mongodb+srv://ege:ege123@cluster0.smbge.gcp.mongodb.net')
class User(Document):
    username=StringField(required=True)
    email=EmailField()
    status=ListField()
    date_created= DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict ={
            "username":self.username,
            "email":self.email
        }
        return json.dumps(user_dict)
    meta={
        "indexes":["username","email"],
        "ordering":["-date_craeted"]
        }

class Offices(Document):
    officeCategoryName=StringField(required=True)
    officeType=StringField(required=True)
    officeUsage=StringField(required=True)
    officeCategory=ListField() #liste şeklinde olacak
    location=StringField(required=True)
    reservations=ReferenceField("Reservation")
    reservation_dates=ListField()

    date_created= DateTimeField(default=datetime.utcnow)

    def json(self):
        office_dict ={
            "officeCategory":self.officeCategory,
            "location":self.location
        }
        return json.dumps(office_dict)
    meta={
        "indexes":["officeCategoryName","officeType","officeUsage","location"],
        "ordering":["-date_craeted"]
        }

class Reservation(Document):
    reservation_dates=DateTimeField()
    reservation_user=ReferenceField("User")
    office=ReferenceField("Offices")

    date_created= DateTimeField(default=datetime.utcnow)

    def json(self):
        reservation_dict ={
            "reservation_dates":self.reservation_dates
        }
        return json.dumps(reservation_dict)
    meta={
        "indexes":["reservation_dates"],
        "ordering":["-date_craeted"]
        }

# Creating Offices
office1=Offices(officeCategoryName="Deniz Manzaralı Köşe Daire",officeUsage="monthly",officeType="Virtual",location="Istanbul",reservation_dates=[ "" ] ).save()

# #Creating Reservation
# def reservation_add(officeCategory):
#     offices=Offices.objects(officeCategoryName=officeCategory)
#     reservations=Reservation(reservation_dates=datetime(2020,10,12), office=offices[0]).save()
#     for res in reservations:
        
#         offices[0].reservation_dates.apppend(datetime(2020,10,12))


# reservation_add("Deniz Manzaralı Köşe Daire")

