# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:41:02 2019

@author: edelk
"""

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
# Get the User object for twitter...
user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)