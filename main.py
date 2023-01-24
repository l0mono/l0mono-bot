import random
import tweepy
import json
import text_gene
import subprocess

with open('token.json') as file:
        object = json.load(file)
        CONSUMER_KEY = object["CK"]
        CONSUMER_SECRET = object["CS"]
        ACCESS_TOKEN = object["AT"]
        ACCESS_SECRET = object["ATS"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#cmd = "wc -l [song.txt]"
#process = subprocess.check_output(cmd.split()).decode().split()[0]

api.update_status(text_gene.file_reader(100))
#api.update_status(status = "hello tweepy with media", filename = 'test.png')