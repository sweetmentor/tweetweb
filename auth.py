import os
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET =  os.getenv('CONSUMER_SECRET')
OAUTH_TOKEN =  os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth    

def get_api():
    auth = get_auth()
    return tweepy.API(auth)
