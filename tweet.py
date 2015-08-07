#!/usr/local/bin/python2.7

from twython import Twython
from config import consumer_key, consumer_secret, access_token, access_token_secret
from index import new_tweet
import logging

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


with open('./past_tweets.log', 'r') as f:
    reader = f.readlines()
    past_tweets = []

    for row in reader:
        past_tweets.append(row)

    test = past_tweets[-1]


    if "Vergennes" in past_tweets[-1]:
        print "hey!"
    else:
        print "fail forever"









# twitter.update_status(status=new_tweet())
# logging.basicConfig(filename='past_tweets.log',level=logging.DEBUG)
# logging.info(new_tweet())
