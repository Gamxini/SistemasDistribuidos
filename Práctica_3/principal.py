#!/usr/bin/python
# -*- coding: utf-8 -*


from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

import twitterAPI
import json

app = Flask(__name__)
GoogleMaps(app)
lista=[]

twitter_api = twitterAPI.oauth_login() 

print ("Tweet hablando sobre el Betis...")

Contenedor_tweet = twitter_api.search.tweets(q='Betis',count=1000,geocode='37.356504,-5.981752,1000km') 

for result in Contenedor_tweet["statuses"]:
    if result["geo"]:
        latitud=result["geo"]["coordinates"][0]
        longitud=result["geo"]["coordinates"][1]
        coordenadas=[latitud,longitud]
        lista.append(coordenadas)

@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side", lat=40.45, lng=3.75, markers=lista, style="height:600px;width:600px;margin:0", zoom=4
    )
    return render_template('template.html', mymap=mymap)

file = open('viva.png','rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'VIVA!'}, {'media[]':data})
print(r.status_code)

if __name__ == "__main__":
    app.run(debug=True)