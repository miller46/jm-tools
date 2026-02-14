import tweepy


class TwitterClient:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_user_tweets(self, username, number_of_tweets=200):
        tweets = self.api.user_timeline(screen_name=username, count=number_of_tweets)
        return tweets

