# Safari Park Twitter Bot

This repository hosts code for the implementation of the Twitter bot [@SafariParkBot](https://twitter.com/SafariParkBot). 

The bot will collect animal images via the Flickr API, and then transform a randomly selected picture using the K-means clustering segmentation algorithms provided through [scikit-image](http://scikit-image.org/).

The bot posts at a user-defined interval. You can also tweet an image at the bot and it will process the image for you. 

## Getting Started

After installing the required packages, clone the GitHub Repository and obtain the 1) [Twitter API Authentication credentials](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth) and a 2) [Flickr API Key](https://www.flickr.com/services/api/misc.api_keys.html).

### Installation

We use the awesome tweepy API to access Twitter. You will also need to install scikit-image and the requests libraries.

```
pip install scikit-image
pip install tweepy
pip install requests
```

## Running the bot

Simply get the bot up and running with: 

```
python safaribot.py
```


## Examples

Below are some of my favorite posts from the bot:


![Lion Original](https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg)
![Lion Transformed](https://pbs.twimg.com/media/DLjeD2vVoAEBTCT.jpg)

![Penguin Original](https://pbs.twimg.com/media/DL_UIX-VwAUwC-E.jpg:large)
![Penguin Transformed](https://pbs.twimg.com/media/DL_UKVnUQAYGbKH.jpg:large)

![Giraffe Original](https://pbs.twimg.com/media/DMHeCb8V4AI4qX-.jpg:large)
![Giraffe Transformed](https://pbs.twimg.com/media/DMHeFK_U8AAlvDj.jpg:large)
