import tweepy as tp
import time
import os
import random 

# credentials to login to twitter api
consumer_key = '3fvyzfvX7UMODfJlzCsAY1mr5'
consumer_secret = 'J5A9MvK6g34L6yLvKFllGZvU10OXZlFlQekUMQLLtFx2iTSa54'
access_token = '1017954633967329280-Uh4BXW8oNPTbFTYmybux1h3XUwEwzB'
access_secret = 'eaOKfLDQfF8B1jQfRZORoleq8PCmC7ciG08ouQT1PudrV'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# os.chdir('souptimebot')
# iterates over pictures in models folder
loop = True
while loop == True:
    api.update_with_media("soup_image.jpg")
    time.sleep(random.randint(28800,86400))