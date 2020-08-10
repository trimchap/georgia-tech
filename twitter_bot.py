import tweepy # see doc.tweepy/en/latest for more info
import time

CONSUMER_KEY = "your c key here"
CONSUMER_SUCCESS = 




api = tweepy.API(auth,wait_on_rate_time=True, wait_on_limit_modify=True)
user = api.me()

search = "wwcodepython"
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print("Tweet liked")
        tweet.favorite()
        print("retweet done")
