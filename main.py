import configparser
import tweepy

# read config
'''config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']'''

api_key = 'JPw3CrXy7WxS5xrC3hZK0iQ6J'
api_key_secret = 'Eb8Mtgp8Gb1fq7cygHA6PTfGHoVL7CZuihrGtHdglU19KF3Z1g'

access_token = '326778044-GSTxUotcJkaU35jw0bWtBysZ6BsSF3FnS1aOcmNT'
access_token_secret = 'WVZgeyixIs1EZTU5xdW9rJpJim5FOqRD6j35uW9eKzSW7'

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
print(public_tweets)