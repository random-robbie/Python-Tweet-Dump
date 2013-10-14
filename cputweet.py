#!/usr/bin/env python
import os
import sys
import tweepy

CONSUMER_KEY = '*****YOUR DATA******'
CONSUMER_SECRET = '*****YOUR DATA******'
ACCESS_KEY = '*****YOUR DATA******'
ACCESS_SECRET = '*****YOUR DATA******'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

api.update_status('My Current Processor Temperature: '+ temp + ' C')