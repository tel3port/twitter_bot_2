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

twitter_ac_1 = "Gidfdz"
twitter_ac_2 = "awedfge1_inc"
twitter_ac_3 = "AdgfGik"
twitter_ac_4 = "fgfwdfgr"
twitter_ac_5 = ""

twitter_account_list = [twitter_ac_1, twitter_ac_2, twitter_ac_3, twitter_ac_4]

write = 'w'
read = "r"

CONSUMER_KEY1 = "vNdmTB5he6nZPMfdJ52alKPUSXE"
CONSUMER_SECRET1 = "R5vdHLRj6c6KZYwPZwMFgregRC0viJCsSXlGDZtmbGC3dMudteq0Wg"
ACCESS_KEY1 = "102722232704451fdhwt7888-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET1 = "dfgsg"

auth1 = tweepy.OAuthHandler(CONSUMER_KEY1, CONSUMER_SECRET1)
auth1.set_access_token(ACCESS_KEY1, ACCESS_SECRET1)
api1 = tweepy.API(auth1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


CONSUMER_KEY2 = "dfgd"
CONSUMER_SECRET2 = "dgg"
ACCESS_KEY2 = "2366758376-dgd"
ACCESS_SECRET2 = "dgd"

auth2 = tweepy.OAuthHandler(CONSUMER_KEY2, CONSUMER_SECRET2)
auth2.set_access_token(ACCESS_KEY2, ACCESS_SECRET2)
api2 = tweepy.API(auth2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

CONSUMER_KEY3 = "dgd"
CONSUMER_SECRET3 = "dgdgdgdf
ACCESS_KEY3 = "dgd-WieCb7mgLnQGt5LJVJCa4B2jQWbAiX"
ACCESS_SECRET3 = "dgfdg"

auth3 = tweepy.OAuthHandler(CONSUMER_KEY3, CONSUMER_SECRET3)
auth3.set_access_token(ACCESS_KEY3, ACCESS_SECRET3)
api3 = tweepy.API(auth3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

CONSUMER_KEY4 = "dgdg"
CONSUMER_SECRET4 = "dgd"
ACCESS_KEY4 = "dgdfg-NrQNabPsR5objNjN1LUeTvMlviboXiS"
ACCESS_SECRET4 = "dgdf"

auth4 = tweepy.OAuthHandler(CONSUMER_KEY4, CONSUMER_SECRET4)
auth4.set_access_token(ACCESS_KEY4, ACCESS_SECRET4)
api4 = tweepy.API(auth4, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


CONSUMER_KEY5 = ""
CONSUMER_SECRET5 = ""
ACCESS_KEY5 = ""
ACCESS_SECRET5 = ""

auth5 = tweepy.OAuthHandler(CONSUMER_KEY5, CONSUMER_SECRET5)
auth5.set_access_token(ACCESS_KEY5, ACCESS_SECRET5)
api5 = tweepy.API(auth5, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api_object_list = [api1, api2, api3, api4]


random_num = randint(1, 5)


def sleep_time():
    t = randint(7, 65)
    print(f"thread sleeping for {t} seconds...")

    time.sleep(t)

    return t


def log_file_writer():
    return logging.basicConfig(filename='errors.log',
                               format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                               datefmt='%Y-%m-%d:%H:%M:%S',
                               level=logging.ERROR)

