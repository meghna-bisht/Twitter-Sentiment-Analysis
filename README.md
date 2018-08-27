# Twitter-Sentiment-Analysis
To detect and analyse sentiments of a tweet

AFINN-111.txt file contains list of some precomputed sentiment score.

To get twitter data :
  1.Go to https://dev.twitter.com/ and login.
  2.Create new app.
  3.Fill the required information.
  4.Click on "Keys and Access Tokens" tab and scroll to the section "Your Access Token".
  5.Create an access token.
  6.Copy Consumer Key(API Key), Consumer Secret(API Secret), Access token and Access token secret to the file twitterstream.py.

Steps to execute the program :
  1.Install Python 2.7.14
  2.Run twitterstream.py
  3.Run tweet_sentiment.py
  4.Run term_sentiment.py

Working : 
If sentiment score for the tweet is less than 0 then the tweet is negative.
Else if score is greater than 0 then tweet is positive.
Else tweet is neutral.
