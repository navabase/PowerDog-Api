#!flask/bin/python
from flask import Flask
from flask import render_template
from flask import request
import calendar
import time
import api
import settings
import os

PORT = os.getenv("PORT","8080")

EMAIL = os.getenv("EMAIL","value does not exist")

HASH = os.getenv("HASH","value does not exist")

apiPWD = os.getenv("PWD","1234")

dog = api.PowerDog(EMAIL,HASH)

app = Flask(__name__)

def StartUTConeDay():
    end = calendar.timegm(time.gmtime())
    return end - 86400 

def EndUTConeDay():
    return calendar.timegm(time.gmtime())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/<key>/<method>')
def Api(key,method):
    print("method",method)
    if(key == apiPWDt): # change the password here
        if(method == "getPowerDogs"):
            return dog.getPowerDogs()
        elif (method == "getInverters"):
            PowerDogId = request.args.get('PowerDogId',default = 1, type = int)
            return dog.getInverters(PowerDogId)

        elif (method == "getCounters"):
            PowerDogId = request.args.get('PowerDogId',default = 1, type = int)
            return dog.getCounters(PowerDogId)

        elif (method == "getSensors"):
            PowerDogId = request.args.get('PowerDogId',default = 1, type = int)
            return dog.getSensors(PowerDogId)

        elif (method == "getPhotovoltaicBorders"):
            PowerDogId = request.args.get('PowerDogId',default = 1, type = int)
            month = request.args.get('month',default = 2020, type = int)
            year = request.args.get('year',default = 1, type = int)
            return dog.getPhotovoltaicBorders(PowerDogId,month,year)
        elif (method == "getSensorData"):
            SensorsId = request.args.get('SensorId',default = 0000, type = int)
            # TODO
        elif (method == "getCounterData"):
            CounterId = request.args.get('CounterId',default = 0000, type = int)
            start = request.args.get('start',default = StartUTConeDay(), type = int)
            end = request.args.get('end',default = EndUTConeDay(), type = int)
            return dog.getCounterData(CounterId,start,end)
    return render_template('notAllowed.html',pwd=key)
if __name__ == '__main__':
    app.run(debug=True,port=PORT)