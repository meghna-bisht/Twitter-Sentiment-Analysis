import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys
import os

#to register our client application with Twitter
api_key = "8K5a6kEfFqb7uryohxiGnH7mG"
api_secret = "cRdswvGdMXwJNfYnHZ3tdpJzBEqNYbxdQBhFjeIvWzbCHr0Hsm"
access_token = "932526626742472704-FokNjnYBWFV7nXjv9GNl1t4APf4R4pJ" 
access_token_secret = "46BLPnZjvTFJalilzDS1YPNuwgm1LB8jrt9bgeHjQ1TYr"

#creating OAuthHandler instance
auth = OAuthHandler(api_key, api_secret)
#to make our data secure we set access token keys
auth.set_access_token(access_token, access_token_secret)
#construct the API instance
#connecting to twitter API using stream
api = tweepy.API(auth)    

#Error handling
if(not api):
    print("Problem connecting to API")
    sys.exit(-1)
    
filename=raw_input("Enter filename in which you want your data to be collected:\n")
#to check if file exits or not
if os.path.isfile(filename):
    print "File already exits.."
    sys.exit(-1)
#Create a class inheriting from StreamListener    
class MyListener(StreamListener):

    print("Please wait atleast 3 minutes for data to accumulate")
    print("Press Ctrl+c to terminate")
    def on_data(self, data):
        try:
            #open a file to collect tweets
            with open(filename, 'a') as f:  
                f.write(data)
                return True
            #to catch exceptions such as KeyBoardInterrupt when Ctrl+c is pressed
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
    
#using class to create stream object
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['One Direction'])
#use filter data based on filter and location
#twitter_stream.filter(track=['weather'],locations=[28.1,76.7,29.1,77.7]) #locations of NEW DELHI




