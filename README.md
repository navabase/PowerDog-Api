# PowerDog-Api
Implementation of the official web-api by [power-dog](https://power-dog.eu) 

## Why we build this Api?
- The originial API is based on [xmlrpc](https://de.wikipedia.org/wiki/XML-RPC) as we tried to build our website with the xmlrpc client we run into several problems.
- What we wanted: easy to use Api without having to deal with frustrating xmlrpc issues and good error responses, because the original API often response with a default error, leaving you in the dark. 
## pre-requirements:
- [python3](https://www.python.org/)
## How to install:
    - clone the repository
    - cd powerdog-api/
    - pip3 install -r requirements.txt
    - python app/app.py

## How to setup the api:
You need to set your Email and Password md5Hash in the .env file
- At first you need to create a **.env** file in the root folder of the project
- the place your email and md5Hash like this (optional you can set a key for your API, the default value is ***1234***):

```
EMIAL=your@email.com
HASH=yourmd5HASH
APIKEY=WhatEverYouLike

```

## How the Api works

The API normally start on Port ***8080*** and hosted on the ***local-ip*** adress of your device [http://localhost:8080](localhost:8080).

All API call's have to go to this adress: [http://localhost:8080/api/v1/](http://localhost:8080/api/v1/)

This is a full API call: [http://localhost:8080/api/v1/**APIKEY**/getPowerDogs](http://localhost:8080/api/v1/1234/getPowerDogs). This returns all Powerdogs which are currently available. 

You need to replace the **APIKEY** with your APIKEY set in the .env file or use the 1234 default Key (not recommended). 

# All available API methods
- ``getPowerDogs`` --> return all Powerdogs
- ``getInverters?PowerDogId=<YourPowerdogID>`` --> returns all Inverters
- ``getCounters?PowerDogId=<YourPowerdogID>`` --> returns all Counter
- ``getSensors?PowerDogId=<YourPowerdogID>`` --> returns all Sensors
-``getPhotovoltaicBorders?PowerDogId=<YourPowerdogID>&year=<year eg. 2020>&month=<eg. 4>``
- ``getCounterData?CounterId=<YourCounterId>`` --> returns data within one day
- ``getCounterData?CounterId=<YourCounterId>&start=<UNIX Format>&end=<UNIX Format>`` --> returns data in specifiyed time | UNIX looks like: 1588248000
