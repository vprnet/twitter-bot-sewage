#!/usr/local/bin/python2.7

import csv

def new_tweet():
    with open('./sewage.csv', 'r') as f:
        reader = csv.reader(f)
        all_incidents = []

        for row in reader:
            all_incidents.append(row)

        if all_incidents[1] == ['No Records Found']:
            tweet_text = False
        else:

            new_tweets = []

            for line in all_incidents:
                tweet_text = line[1][:10] + ": " + line[5] + ", " + line[4] + " " + "(" + line[6] + " estimated)"
                new_tweets.append(tweet_text)

            return new_tweets
