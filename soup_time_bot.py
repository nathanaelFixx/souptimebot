import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = '0FPbIt83beNU8RWCRI1uaV9hh'
consumer_secret = 'IKW07eVfulTLm5s150v1fbD28gEUNERJyMJWUtS8eTKgU5DQay'
access_token = '1017954633967329280-FzlzI4CN6oBmhV4v2oWZnDyDmm8JKt'
access_secret = 'aE5CsM7sHE7zXxz8lHUiU6FJBNAq6jzvWr6xK5r33XD3a'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('soup')
# iterates over pictures in models folder
loop = True
while loop == True:
    api.update_with_media("soup_image.jpg")
time.sleep(60)