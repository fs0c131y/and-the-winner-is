import sys
from random import randint

import tweepy

CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"
ACCESS_TOKEN = "xxx"
ACCESS_SECRET = "xxx"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


def main():
    if len(sys.argv) > 1:
        status_id = sys.argv[1]

        api = tweepy.API(auth)
        retweets_list = api.retweets(status_id)

        screen_names = []
        for retweet in retweets_list:
            screen_names.append(retweet.user.screen_name)

        print(screen_names[randint(0, len(screen_names))])
    else:
        print('Usage: python andthewinneris.py [status_id]')


if __name__ == '__main__':
    main()
