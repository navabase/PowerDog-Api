#!/path/to/python 

import xmlrpc.client
import time
server = xmlrpc.client.ServerProxy('http://api.power-dog.eu/')

class PowerDog():
    def __init__(self,email,md5hash):
        print("Getting API Key")
        print("KEY;", email,md5hash)
        self.server = xmlrpc.client.ServerProxy('http://api.power-dog.eu/')
        self.apiKey = self.api(email,md5hash)
        time.sleep(10)

	
    def api(self,email,md5hash):
        print("vlaues:",email,md5hash)
        print("server",self.server)
        response = server.getApiKey(email,md5hash)
        return response

    def getPowerDogs(self):
        response = self.server.getPowerDogs(self.apiKey)
        return response

    def getInverters(self,server,apiKey,PowerDogId):
        response = server.getInverters(apiKey,PowerDogId)
        return response

    def getSensors(self,PowerDogId):
        response = self.server.getSensors(self.apiKey, PowerDogId)
        return response

    def getStringData(self,sensorId, num, start, end):
        response = self.server.getStringData(self.apiKey,sensorId, num, start,end)
        return response

    def getSensorData(self,sensorId, n,start, end):
        response = self.server.getSensorData(self.apiKey,sensorId,n)
        return response

    def  getPhotovoltaicBorders(self,PowerDogID,month,year):
        response = self.server.getPhotovoltaicBorders(self.apiKey,PowerDogID, month, year)
        return response

    def getStringDayData(self, sensorId, StringNum, day_from,day_to,month,year):
        response = self.server.getStringDayData(self.apiKey,sensorId, StringNum, day_from, day_to, month, year)
        return response

    def getCounters(self, server, apiKey,PowerDogID):
        response = server.getCounters(apiKey,PowerDogID)
        return response

    def getCounterData(self, server, apiKey,counterId,start,end):
        response = server.getCounterData(apiKey,counterId,start,end)
        return response

