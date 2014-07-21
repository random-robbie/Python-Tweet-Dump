Python-Tweet-Dump
=================

Dumping My Twitter Python Scripts for any one to alter or use.

Needed to Install
----

```
sudo apt-get update
sudo apt-get install python-setuptools -y
sudo pip install websocket-client requests python-magic tweepy

All Scripts will require the following to be changed.


```
consumer_key, consumer_secret, access_token, access_token_secret = "consumer key", "consumer secret", "access token", "access token secret"
```

Get that from http://dev.twitter.com for your application




Tweet.py
--------

Ensure you have entered the correct details and then to use it do 

```
python ./Tweet.py "My Message"
```

This will tweet what ever you want



DMMyip
------

This sends a DM with the Local IP you can change the end of the message to ETH0 if your not using wireless

change the following to the screen name to get the DM

```
screen_name='CHANGEME'
```



