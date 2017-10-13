"""
This module encapsulates the underlying logic for the Twitter SafariParkBot.
The bot will post an animal image from Flickr at a set-interval, while
also listening for any tweets directed to it. You can tweet an image at the
bot and it will process the image for you.
"""

from io import BytesIO
import random
import time

#privateappconfig file contains twitter API access keys, FLICKR api key
from privateappconfig import *

import tweepy
import requests
from skimage import io
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
        """Initializes a stream listener, subscribes to tweets directed at it"""
        self.__listener = Listener(self.__api)
        tweepy.Stream(self.__auth, self.__listener).filter(track=['@SafariParkBot'], async=True)

    def post_animal_picture(self):
        """Uses FLICKR API to update twitter feed with transformed picture"""
        url = 'https://api.flickr.com/services/rest/'
        params = dict(
            api_key=FLICKR_API_KEY,
            text='animals',
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
    authentication = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authentication.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    bot = SafariBot(authentication)
    bot.listen_for_tweets()
    print 'Listening for tweets'
    while True:
        bot.post_animal_picture()
        print 'Posted new picture!'
        time.sleep(600)
