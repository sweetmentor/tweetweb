import tweepy
from auth import get_api

api = get_api()


def search_for_tweets(query, count):
    return [{'id': status.id,'text': status.text} for status in tweepy.Cursor(api.search, q=query).items(count)]
    
