"""
This module looks for images in a filtered stream of Twitter data.
When an image is identified, the image is transformed via image processing algorithms
and then posted on Twitter.
"""

from io import BytesIO
from tweepy.streaming import StreamListener, TweepError
from imgsegmenter import ImageSegmenter
import requests
from skimage import io

class Listener(StreamListener):
    """
    Class that implements the Tweepy StreamListener class.
    """
    def __init__(self, api):
        self.api = api
        self.__imgsegmenter = ImageSegmenter()
        
    def on_status(self, status):
        """Override base class method, this is a method handler for the Stream event"""
        try:
            if 'media' in status.entities:
                for image in status.entities['media']:
                    self._tweet_image(image['media_url'], status.user.screen_name, status.id)
        except TweepError as err:
            print err.reason()

    def _tweet_image(self, url, user, statusid):
        """Internal function that gets the image URL from the stream, transforms and then retweets it"""
        orig = 'original_image.png'
        new = 'new_image.png'

        resp = requests.get(url, stream=True)
        if resp.status_code == 200:
            i = io.imread(BytesIO(resp.content))
            io.imsave(orig, i)
            img = self.__imgsegmenter.transform(i)
            io.imsave(new, img)
            self.api.update_with_media(new, status='@{0}'.format(user), in_reply_to_status_id=statusid)