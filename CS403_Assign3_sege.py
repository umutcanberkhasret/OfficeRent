

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

m=[]
SEAT_LIMIT=100
seats = []
reservation_no = 0
reservations=[]
salon1 = []
salon2 = []
salon3 = []


class Movies(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        name = json_data['name']
        date = json_data['date']
        time = json_data['time']   
        
        for i in salon1:
            if date == i['date'] and time == i['time']:
                for i2 in salon2:
                    if date == i2['date'] and time == i2['time']:
                        for i3 in salon3:
                            if date == i2['date'] and time == i2['time']:
                                return {}, 404
                        movie = {'name': name, 'date': date, 'time': time, 'screen_no': 3}
                        m.append(movie)
                        return {"screen_no": 3}, 201
                movie = {'name': name, 'date': date, 'time': time, 'screen_no': 2}
                m.append(movie)
                return {"screen_no": 2}, 201                    
        
        movie = {'name': name, 'date': date, 'time': time, 'screen_no': 1}        
        m.append(movie)    
        
        return {"screen_no": 1}, 201
        
    def get(self):
        return m
            
api.add_resource(Movies, '/movies')

class Movie_arama(Resource):    
        
    def get(self, name, date):
        print(name, date, type(date))
        for i in m:
            #print(i['name'], i['date'])
            
            if i['name'] == name and i['date'] == date:
                return m,200 
        return {"a":1},404
    
    def delete(self, name, date):
        #print("deleting: ", name, date)
        for i in m:
            if i['name'] == name and i['date'] == date:
                m.remove(i)
                
                if i['screen_no']==1:
                    for a in salon1:
                        if a['name'] == name and a['date'] == date:
                            salon1.remove(a)
                            
                elif i['screen_no']==2:
                    for a in salon2:
                        if a['name'] == name and a['date'] == date:
                            salon2.remove(a)
                            
                elif i['screen_no']==3:
                    for a in salon3:
                        if a['name'] == name and a['date'] == date:
                            salon3.remove(a)                          
                            
                return {"a":1},200
        return {},404
            
api.add_resource(Movie_arama, '/movies/<string:name>/<string:date>')



class ticket(Resource):
    def post(self):
        global reservation_no
        json_data = request.get_json(force=True)
        name = json_data['name']
        date = json_data['date']
        time = json_data['time']          
 
        for i in m:
            
            if json_data == i:
                
                for a in seats:
                    
                    if ( a['name'] == name and a['date']== date ) and a['time'] == time :
                        
                        if a['seat_no'] >= SEAT_LIMIT:
                            return {"a": 1}, 409
                        else:
                            a['seat_no'] = a['seat_no'] +1
                            res={'name': name, 'date': date, 'time': time, 'screen_no': 1, 'seat_no':a['seat_no'], 'reservation_no': reservation_no}
                            reservations.append(res)
                            #a['reservation_no'] = reservation_no                            
                            reservation_no = reservation_no + 1
                            return {"reservation_no": reservation_no-1}, 201
                
                res = {'name': name, 'date': date, 'time': time, 'screen_no': 1, 'seat_no':1} 
                seats.append(res)
                res1 = {'name': name, 'date': date, 'time': time, 'screen_no': 1, 'seat_no':1, 'reservation_no': reservation_no}
                reservations.append(res1)
                #global reservation_no
                reservation_no = reservation_no + 1
                
                return {"reservation_no": reservation_no-1}, 201
            
        return {"a": 1}, 404
        
    def get(self):
        
        try:
            json_data = request.get_json(force=True)
        except Exception as e:
            return reservations
        
        res_no = json_data['reservation_no']
        for i in reservations:
            if res_no == i['reservation_no']:
                if i['seat_no'] == -1:
                    return {"a": 1}, 404
                return i, 200
        return {"a": 1}, 404
    
    def put(self):
        json_data = request.get_json(force=True)
        res_no = json_data['reservation_no']
        seat_no = json_data['seat_no']
        for i in reservations:
            if res_no == i['reservation_no']:
                for a in reservations:
                    if ( a['name'] == i['name']and a['date']== i['date'] ) and a['time'] == i['time']:
                        if seat_no <= a['seat_no']:
                            return {"a":1}, 409
                        
                return {"a":1}, 200
        return {"a":1}, 404
    
    def delete(self):
        json_data = request.get_json(force=True)
        res_no = json_data['reservation_no']
        
        for i in reservations:
            if res_no == i['reservation_no']:
                
                if i['seat_no'] != -1:
                    i['seat_no'] = -1
                    return {"a":1}, 200
                else:
                    return {"a":1}, 404
        return {"a":1}, 404
            
api.add_resource(ticket, '/ticket')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
