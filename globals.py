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
twitter_ac_3 = "AudioGik"
twitter_ac_4 = "wax_gr"
twitter_ac_5 = ""

twitter_account_list = [twitter_ac_1, twitter_ac_2, twitter_ac_3, twitter_ac_4]

write = 'w'
read = "r"

CONSUMER_KEY1 = "vNdmTB5he6nZPMJ52alKPUSXE"
CONSUMER_SECRET1 = "R5vdHLRj6c6KZYwPZwMFRC0viJCsSXlGDZtmbGC3dMudteq0Wg"
ACCESS_KEY1 = "1027222327044517888-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET1 = "X513wVVUW3yyIE3HnEmSEaGdYWsmHIcVBeHUGUdX9TcvI"

auth1 = tweepy.OAuthHandler(CONSUMER_KEY1, CONSUMER_SECRET1)
auth1.set_access_token(ACCESS_KEY1, ACCESS_SECRET1)
api1 = tweepy.API(auth1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


CONSUMER_KEY2 = "uin4wl1ooepMlO1u0IpHBRj6H"
CONSUMER_SECRET2 = "mPr3qE6KaFOTulBhGoIKEFZC3WQ1A2NTBEW6ra9GqrhLE9XPFu"
ACCESS_KEY2 = "2366758376-81og6kl876MdZJv6wea8GDPdQhevevvyDa4gu40"
ACCESS_SECRET2 = "HOGarTpNROkVoYQ9w57gwsZilPS4zG0st9hA4giUZPAfk"

auth2 = tweepy.OAuthHandler(CONSUMER_KEY2, CONSUMER_SECRET2)
auth2.set_access_token(ACCESS_KEY2, ACCESS_SECRET2)
api2 = tweepy.API(auth2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

CONSUMER_KEY3 = "bN0DA01VN64oi1iRK2svATG7E"
CONSUMER_SECRET3 = "5tyD0qdCuBABVqo9gohDjH9R16XyrkJwCVGqyL6JpYenxw2tMJ"
ACCESS_KEY3 = "1171908782642913293-WieCb7mgLnQGt5LJVJCa4B2jQWbAiX"
ACCESS_SECRET3 = "YDPN8kv8vp8GhCB7ZL5CC15ACdzKEiHil45BZOXeK6POb"

auth3 = tweepy.OAuthHandler(CONSUMER_KEY3, CONSUMER_SECRET3)
auth3.set_access_token(ACCESS_KEY3, ACCESS_SECRET3)
api3 = tweepy.API(auth3, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

CONSUMER_KEY4 = "dXPf4e6JLFwQ5zjfNelWga9At"
CONSUMER_SECRET4 = "AbNdHFIaBqKtOFzbBotr4PPE7XsaMeKAgaBzfLCEzIvx2FuqSX"
ACCESS_KEY4 = "998204500950253568-NrQNabPsR5objNjN1LUeTvMlviboXiS"
ACCESS_SECRET4 = "GkxjJPk7A0zFgsYj6zItjE48qyZ0YtqcLUq9UVq1ZEDNT"

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

