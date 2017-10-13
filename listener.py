"""
Module implements a Twitter stream listener for animal images
"""

from tweepy.streaming import StreamListener, TweepError
from imgsegmenter import ImageSegmenter
import requests
from io import BytesIO
from skimage import io

class Listener(StreamListener):
    def __init__(self, api):
        self.api = api
        self.__imgsegmenter = ImageSegmenter()
        
    def on_status(self, status):
        """Override base class method for posting animal methods"""
        try:
            if 'media' in status.entities:
                for image in status.entities['media']:
                    self._tweet_image(image['media_url'], status.user.screen_name, status.id)
        except TweepError as e:
            print e.reason()

    def _tweet_image(self, url, user, id):
        orig = 'original_image.png'
        new = 'new_image.png'

        resp = requests.get(url, stream=True)
        if resp.status_code == 200:
            i = io.imread(BytesIO(resp.content))
            io.imsave(orig, i)
            img = self.__imgsegmenter.transform(i)
            io.imsave(new, img)
            self.api.update_with_media(new, status='@{0}'.format(user), in_reply_to_status_id=id)