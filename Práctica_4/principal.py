#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Francisco José Pastor & Antonio Gambín Iñigo'

import twitter
from twitterAPI import *
from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map


app = Flask(__name__)
GoogleMaps(app)

def getTweetsSearch(busqueda):
    twit = oauth_login() 
    limite = "40.0000,-3.000,500km"

    twit = oauth_login() 
    Contenedor_tweet = twit.search.tweets(q=busqueda,count=1000, geocode=limite) 
    res=[]
    for result in Contenedor_tweet["statuses"]:
        if result["geo"]:
            coordenadas=[result["geo"]["coordinates"][0],result["geo"]["coordinates"][1]]
            res.append(coordenadas)
    return res


@app.route("/search", methods=['POST'])
def buscar():
    termino = request.form['text'] 
    coordenadas = getTweetsSearch(termino)
    mapa = Map(identifier="view-side", lat=40, lng=-3, markers=coordenadas, style="height:500px;width:700px;margin:0", zoom=6)
    return render_template('mapa.html', mymap=mapa)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)