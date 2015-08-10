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

    scraped_tweet = new_tweet()
    latest_spill = str(scraped_tweet)

    if latest_spill in past_tweets[-1] or past_tweets[-2]:
        print "Already been tweeted."
    else:
        logging.basicConfig(filename='past_tweets.log', level=logging.INFO)
        logging.info(latest_spill)
        twitter.update_status(status=latest_spill)
        print "New tweet tweeted."
