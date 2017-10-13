"""
Module for the Safari Park Twitter Bot.
You can tweet an image at the bot.
"""

import tweepy
import requests
import random
from io import BytesIO
from skimage import io
from privateappconfig import *
from imgsegmenter import ImageSegmenter
from listener import Listener

class SafariBot(object):
    """Encapsulates functions for the twitter bot"""
    def __init__(self, authorization):
        self.__auth = authorization
        self.__api = tweepy.API(self.__auth)
        self.__listener = None
        self.__imgsegmenter = ImageSegmenter()
        self.__clf = None

    def listen_for_tweets(self):
        """Initializes a stream listener for the bot"""
        self.__listener = Listener(self.__api)
        tweepy.Stream(self.__auth, self.__listener).filter(track=['@SafariParkBot'], async=True)

    def post_animal_picture(self):
        """Uses Twitter API to update timeline with a new picture"""
        url = 'https://api.flickr.com/services/rest/'
        params = dict(
            api_key=FLICKR_API_KEY,
            text='safari',
            tags='animals',
            format='json',
            nojsoncallback=1,
            method='flickr.photos.search',
        )

        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            photos = resp.json()['photos']['photo']
            photo = random.choice(photos)
            url =  "https://farm{}.staticflickr.com/{}/{}_{}.jpg".format(str(photo['farm']), photo['server'], photo['id'], photo['secret'])

            orig = "orig.png"
            new = "new.png"
            resp = requests.get(url, stream=True)
            if resp.status_code == 200:
                i = io.imread(BytesIO(resp.content))
                io.imsave(orig, i)
                img = self.__imgsegmenter.transform(i)
                io.imsave(new, img)
                self.__api.update_with_media(new, status=url)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    bot = SafariBot(auth)
    bot.post_animal_picture()
