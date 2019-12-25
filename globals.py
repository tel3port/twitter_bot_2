import tweepy
from random import randint
import logging
import time

value_holder_file = 'last_seen_id.txt'

minion_ids_csv = "minion_and_ids.csv"
downloaded_tweets_csv = "downloaded_tweets.csv"
tweets_ids_csv = "ht_tweets_and_ids.csv"
follower_ids_csv = "follower_and_ids.csv"
usa_giveaway = "https://cool-giveaways.weebly.com/"

twitter_ac_1 = "GikSoundz"
twitter_ac_2 = "awesome1_inc"
twitter_ac_3 = ""
twitter_ac_4 = ""
twitter_ac_5 = ""


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

