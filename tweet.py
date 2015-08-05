#!/usr/local/bin/python2.7

from twython import Twython
from config import consumer_key, consumer_secret, access_token, access_token_secret
from index import new_tweet

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

twitter.update_status(status=new_tweet())
