################################################
# This Sends a DM of the Lan IP
#
#
################################################
import tweepy, sys
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

LAN = get_ip_address('eth0')	
WLAN = get_ip_address('wlan0')
consumer_key, consumer_secret, access_token, access_token_secret = "consumer key", "consumer secret", "access token", "access token secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print "Successfully logged in as " + api.me().name + "."
api.send_direct_message(screen_name='CHANGEME',text='Hello Your Local IP is' + WLAN)
print "Successfully Sent DM"
