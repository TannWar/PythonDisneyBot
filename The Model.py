# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'PzwAsjbHroZXZPkiIski5gQcb'
consumer_secret = 'ECkEicG0NL5tKy0RUkkSzV3W5lJP9TNEEpfeBwG04BVbM62SdI'
access_token = '1250153682638782464-9DF8ElkvsCF1IKJiBu3JJVI9sBaYjd'
access_secret = 'KwNnOXhGp2TIcpZHvOR3hmlhkhrOR6CFQGAUK5bG8rtys'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('disneyland')

# iterates over pictures in models folder
for disneyland_image in os.listdir('.'):
    api.update_with_media(disneyland_image)
    time.sleep(60)
