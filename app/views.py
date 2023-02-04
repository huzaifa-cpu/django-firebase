from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
import pyrebase
from django.http import JsonResponse

config={
    "apiKey": "AIzaSyAoi-GYlUpStQ08pQnk2hmA-Wiv9Cd4WvY",
    "authDomain": "thermosoft1-da425.firebaseapp.com",
    "databaseURL": "https://thermosoft1-da425-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "thermosoft1-da425",
    "storageBucket": "thermosoft1-da425.appspot.com",
    "messagingSenderId": "435255063272",
    "appId": "1:435255063272:web:8c11e4f6bc58188d410f5d",
    "measurementId": "G-K26VL8HFP2"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        hum = database.child('ESP32_APP').child('TEMPERATURE1').get().val()
        temp = database.child('ESP32_APP').child('TEMPERATURE2').get().val()
    
        data = {
            'temperature1':hum,
            'temperature2':temp
        }
        return JsonResponse(data)
