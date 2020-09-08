from mongoengine import *
from datetime import datetime
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
    officeCategory=StringField(required=True)
    location=StringField(required=True)
    status=ListField()
    reservation_dates=ListField()
    date_created= DateTimeField(default=datetime.utcnow)

    def json(self):
        office_dict ={
            "officeCategory":self.officeCategory,
            "location":self.location
        }
        return json.dumps(office_dict)
    meta={
        "indexes":["officeCategory","location"],
        "ordering":["-date_craeted"]
        }

class Reservation(Document):
    reservation_type=StringField()
    reservation_dates=StringField()
    reservation_user=ReferenceField("User")
    office=ReferenceField("Offices")

    date_created= DateTimeField(default=datetime.utcnow)

    def json(self):
        reservation_dict ={
            "reservation_type":self.reservation_type,
            "reservation_dates":self.reservation_dates
        }
        return json.dumps(reservation_dict)
    meta={
        "indexes":["reservation_type","reservation_dates"],
        "ordering":["-date_craeted"]
        }




reservations=Reservation(reservation_type="ART",reservation_dates="12.12").save()

Reservation.objects()
