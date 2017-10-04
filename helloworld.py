"""
First time setup using tweepy API
"""
import sys
import tweepy
from config import * 

#enter the corresponding information from your Twitter application:
class TwitterApp(object):
    """ Encapsulates Twitter requests"""
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet_message(self,text):
        """Wrapper for tweeting"""
        self.api.update_status('Hello world from my app!')