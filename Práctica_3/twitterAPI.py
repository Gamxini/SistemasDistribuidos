#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ = 'Gambin Inigo Antonio - Pastor Aznar Francisco Jose'

import twitter
import io
import json

#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'wJbzaGN6xGBRA1VX9PRReQLHg'
    CONSUMER_SECRET = 'EdfivNgnO6h5RiKnCabiqDvd42UY0d1QlKKKTc4ctSCLIRJszh'
    OAUTH_TOKEN = '3092945518-5ftkt3E9xbILVCUiTW412kw7YLytaaVKKSxra2X'
    OAUTH_TOKEN_SECRET = '55JhrxC9DDlSxi5JPCvrwyVsIn7BAtjPXHPQ4csUSNiVf'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api