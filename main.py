import random
import tweepy
import json

with open('token.json') as file:
    object = json.load(file)
    CONSUMER_KEY = object["CK"]
    CONSUMER_SECRET = object["CS"]
    ACCESS_TOKEN = object["AT"]
    ACCESS_SECRET = object["ATS"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


tweetlist=["Hello","Hey, l085440.","Moi!!!!","THX!"]

api.update_status(random.choice(tweetlist))