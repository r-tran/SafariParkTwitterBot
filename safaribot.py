"""
Module for the Safari Park Twitter Bot.
You can tweet an image at the bot.
"""

import tweepy

from privateappconfig import *
from animallistener import AnimalListener
from animalimageclf import AnimalImageClassifier

class SafariBot(object):
    """Encapsulates functions for the twitter bot"""
    def __init__(self, authorization):
        self.__auth = authorization
        self.__api = tweepy.API(self.__auth)
        self.__listener = None
        self.__imgprocessor = None
        self.__clf = None
    
    def listen_for_tweets(self):
        """Initializes a stream listener for the bot"""
        self.__listener = AnimalListener()
        tweepy.Stream(self.__auth, self.__listener).filter(track=['@SafariParkBot'])
    
    def post_animal_picture(self):
        """Uses Twitter API to update timeline with a new picture"""
        pass

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    bot = SafariBot(auth)
    bot.listen_for_tweets()
