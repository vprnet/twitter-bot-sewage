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

    new_tweet = new_tweet()
    latest_spill = str(new_tweet)

    print past_tweets

    if latest_spill in past_tweets[-1]:
        print "this tweet has already been tweeted"
    else:
        print "tweet tweeted"
        logging.basicConfig(filename='past_tweets.log' ,level=logging.INFO)
        logging.info(latest_spill)
        latest_spill = "test, sorry taylor"
        # twitter.update_status(status=latest_spill)
