import tweepy
from random import randint
import logging
import time

tweets_csv = "tweets.csv"
handles_txt = 'handles.txt'
dld_tweets_txt = "downloaded_handles.txt"
value_holder_file = 'last_seen_id.txt'

write = 'w'

read = "r"

CONSUMER_KEY = "vNdmTB5he6nZPMJ52alKPUSXE"
CONSUMER_SECRET = "R5vdHLRj6c6KZYwPZwMFRC0viJCsSXlGDZtmbGC3dMudteq0Wg"
ACCESS_KEY = "1027222327044517888-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET = "X513wVVUW3yyIE3HnEmSEaGdYWsmHIcVBeHUGUdX9TcvI"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


random_num = randint(1, 5)


def sleep_time():
    t = randint(1, 5)
    print(f"thread sleeping for {t} seconds...")

    time.sleep(t)

    return t


def log_file_writer():
    return logging.basicConfig(filename='errors.log',
                               format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                               datefmt='%Y-%m-%d:%H:%M:%S',
                               level=logging.ERROR)

