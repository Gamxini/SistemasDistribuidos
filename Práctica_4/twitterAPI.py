#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ = 'Gambin Inigo Antonio - Pastor Aznar Francisco Jose'

import twitter
import io
import json

#Funcion para la conexion.
def oauth_login():
    CONSUMER_KEY = 'wJbzaGN6xGBRA1VX9PRReQLHg'
    CONSUMER_SECRET = 'EdfivNgnO6h5RiKnCabiqDvd42UY0d1QlKKKTc4ctSCLIRJszh'
    OAUTH_TOKEN = '3092945518-5ftkt3E9xbILVCUiTW412kw7YLytaaVKKSxra2X'
    OAUTH_TOKEN_SECRET = '55JhrxC9DDlSxi5JPCvrwyVsIn7BAtjPXHPQ4csUSNiVf'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()

def getTweetsSearch(busqueda):
	twitter_api =  oauth_login()
	#Limitamos la busqueda a Espana
	localizacion = "40.2085,-3.713,497mi"

	tweets = twitter_api.search.tweets(q=busqueda, count=1000, geocode=localizacion)

	aux = json.dumps(tweets, indent = 1)
	it = json.loads(aux)

	resultado = []
	for i in it['statuses']:
		if i['coordinates'] is not None:
			resultado.append(i['coordinates']['coordinates'][1])
			resultado.append(i['coordinates']['coordinates'][0])

	resultado = zip(resultado[0::1], resultado[1::2])
	return resultado

