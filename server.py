from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import requests 

# data processing
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# load utilities
import sys
sys.path.append('./utils/')
import json
import parsedate
import histogram

# date processing 

from datetime import date, timedelta

app = Flask(__name__)
CORS(app)
print(__name__)

@app.route('/')
def initial():
    return 'OK!'

@app.route('/health')
def health():
    return 'OK!'

@app.route('/getKinos')
def getKinos():
    print('1')
     # here we want to get the value of user (i.e. ?user=some-value)
    date = request.args.get('date')
    # # api-endpoint 
    URL = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{date}/{date}"
  
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
  
    # extracting data in json format 
    data = r.json()
    return data

@app.route('/getHist')
def getHist():

    # http://localhost:5000/getHist?startDate=2020-01-01&endDate=2020-01-01&limit=180
    # http://localhost:5000/getHist?startDate=2020-01-01&endDate=2020-01-05&limit=180
    kinoBonus=[]
    kinoData=[]
     # here we want to get the value of user (i.e. ?user=some-value)
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    limit = request.args.get('limit')

    startDate=parsedate.parse_date(startDate)
    print('startDate',startDate)

    endDate=parsedate.parse_date(endDate)
    print('endDate',endDate)

    # # edate = date(2008, 9, 15)   # end date

    delta = endDate - startDate       # as timedelta

    print('delta', delta)
    i=1
    for i in range(delta.days + 1):
        
        day = startDate + timedelta(days=i)
        URL = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{day}/{day}?limit={limit}"
        r = requests.get(url = URL) 
        data = r.json()
        print('---------------------------------------------------------------------')
        content=data["content"] 
        for draw in content: 
            kino=draw["winningNumbers"]["bonus"][0]
            kinoBonus.append(kino)
            kinoData.append({
               "kino":kino,
               "drawTime":draw["drawTime"],
               "drawId":draw["drawId"]
            })
        print('totalElements',data["totalElements"])
        print('loop:',i)
    
    print('kinoBonus:',kinoBonus)
    print('------------------')
    kinoBonus.sort()
    print('kinos sorted:',kinoBonus)
    print('kinos length:',len(kinoBonus))
    '''
    Converting kinos to json
    ''' 
    histogramResults=histogram.computeHist(kinoBonus)
    jsonKinos = json.dumps(kinoBonus)

    return json.dumps({
        "histogramResults":histogramResults,
        "kinos":kinoBonus,
        "kinoData":kinoData

    })
