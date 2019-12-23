import tweepy
import globals as gls
import csv
import logging
import glob

print("starting my engines...")

minions_dict = {}
dld_tweet_dict = {}
ht_tweet_dict = {}
follower_id_dict = {}

handle_source_list = ["FactSoup",
                      "Casey",
                      "ithinkthatway",
                      "#Christmas"
                      ]
hashtag_list = ["#USA",
                "#Christians",
                "#Christmas",
                "#TwitterMomentOfTheDecade"
                ]
tweet_source_list = ["FactSoup",
                     "Fact",
                     "SmiIe",
                     "ithinkthatway"]
image_list = glob.glob("media/*")


def dict_loader():  # loads all downloaded data into respective dictionaries

    try:
        with open("minion_and_ids.csv", gls.read) as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:

                minions_dict[single_row[0][:-1]] = single_row[1]  # adding minion data as key value pairs

    except IOError as x:
        print("problem reading the minions_and_ids csv")
        logging.error('Error occurred ' + str(x))
    except Exception as e:
        print("the problem is: ", e)
        logging.error('Error occurred ' + str(e))

    finally:
        print(minions_dict)
        pass

    first_line = True

    try:
        with open("downloaded_tweets.csv", gls.read) as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop

                dld_tweet_dict[single_row[0][:-1]] = single_row[2]  # adding minion data as key value pairs

    except IOError as x:
        print("problem reading the downloaded_tweets csv")
        logging.error('Error occurred ' + str(x))
    except Exception as e:
        print("the problem is: ", e)
        logging.error('Error occurred ' + str(e))

    finally:
        print(dld_tweet_dict)
        pass

    first_line = True

    try:
        with open("tweets_&_ids.csv", gls.read) as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop

                ht_tweet_dict[single_row[0][:-1]] = single_row[1]  # adding minion data as key value pairs

    except IOError as x:
        print("problem reading the tweets_&_ids csv")
        logging.error('Error occurred ' + str(x))
    except Exception as e:
        print("the problem is: ", e)
        logging.error('Error occurred ' + str(e))

    finally:
        print(ht_tweet_dict)
        pass

    first_line = True

    try:
        with open("follower_and_ids.csv", gls.read) as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop

                follower_id_dict[single_row[0][:-1]] = single_row[1]  # adding minion data as key value pairs

    except IOError as x:
        print("problem reading the tweets_&_ids csv")
        logging.error('Error occurred ' + str(x))
    except Exception as e:
        print("the problem is: ", e)
        logging.error('Error occurred ' + str(e))

    finally:
        print(follower_id_dict)
        pass


def save_last_seen_id(my_id, my_file):
    f_write = open(my_file, 'w')
    f_write.write(str(my_id))
    f_write.close()
    return


def get_last_seen_id(my_file):
    f_read = open(my_file, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


# gets a list of all followers from a given user
def follower_extractor(follower_and_id_csv, single_handle):
    print(" follower_extractor() starting...")
    gls.log_file_writer()
    try:
        fol_id_csv = open(follower_and_id_csv, gls.write)
        csv_writer = csv.writer(fol_id_csv)
        for single_follower in tweepy.Cursor(gls.api.followers, screen_name=single_handle).items():
            print(f"{single_follower.id} - {single_follower.screen_name}")
            csv_writer.writerow([str(single_follower.id)+'x', single_follower.screen_name.encode('utf-8')])
            print("row (hopefully )written into csv")

    except tweepy.TweepError as em:
        logging.error('Error occurred ' + str(em))
        print('Error occurred ' + str(em))

    finally:
        print(" follower_extractor() done")

        pass


# extracts all tweets of a given user
def tweet_fetcher(screen_name):
    print(" tweet_fetcher() starting...")

    # initialize a list to hold all the tweepy Tweets
    all_tweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = gls.api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    all_tweets.extend(new_tweets)

    print(all_tweets)

    # save the id of the oldest tweet less one
    oldest = all_tweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % oldest)

        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = gls.api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        all_tweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = all_tweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(all_tweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    out_tweets = [[tweet.id_str+'x', tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]

    # write the csv
    with open("downloaded_tweets.csv", gls.write) as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(out_tweets)

    pass


# this loop gets a list handles and ids of everyone i follow
def my_minion_extractor(my_minion_csv, my_twitter_ac):
    print(" minion_extractor() starting...")
    gls.log_file_writer()
    try:
        minion_csv = open(my_minion_csv, gls.write)
        csv_writer = csv.writer(minion_csv)
        for single_minion in tweepy.Cursor(gls.api.followers, screen_name=my_twitter_ac).items():
            print(f"minion id: {single_minion.id} -  minion name: {single_minion.screen_name}")
            csv_writer.writerow([str(single_minion.id)+'x', single_minion.screen_name.encode('utf-8')])
            print("row (hopefully )written into csv")

    except tweepy.TweepError as ev:
        logging.error('Error occurred ' + str(ev))
        print('Error occurred ' + str(ev))

    finally:
        print("minion extraction done")

        pass


# only sends dms to people that follow me
def dm_sender(minion_id, text):
    print("starting dm_sender()")

    gls.log_file_writer()
    try:
        gls.api.send_direct_message(minion_id, text)

    except tweepy.TweepError as ue:
        logging.error('Error occurred ' + str(ue))
        print('Error occurred ' + str(ue))

    except Exception as ep:
        logging.error('Error occurred ' + str(ep))
        print('Error occurred ' + str(ep))

    finally:
        pass


# sends out text tweets
def tweet_sender(single_handle, single_tweet, single_hashtag):
    print("starting tweet_sender()")

    gls.log_file_writer()

    try:
        gls.api.update_status(f'hey @{single_handle}, {single_tweet} {single_hashtag}')

        gls.sleep_time()

    except tweepy.TweepError as ed:
        logging.error('Error occurred ' + str(ed))
        print('Error occurred ' + str(ed))

    finally:
        pass

    print("tweet_sender() has terminated")


# follows the handle given
def twitter_user_follower(single_handle):
    print("starting twitter_user_follower()")

    gls.log_file_writer()
    try:

        print(f"creating friendship with: {single_handle}")

        gls.api.create_friendship(screen_name=single_handle)

        gls.sleep_time()

    except tweepy.TweepError as ef:
        logging.error('Error occurred ' + str(ef))
        print('Error occurred ' + str(ef))

    except Exception as eg:
        logging.error('Error occurred ' + str(eg))

    finally:
        pass

    print("twitter_user_follower() has terminated")


# this replies to all mentions in a loop
def custom_replier():
    gls.log_file_writer()

    try:
        print("replying to custom mentions...")
        last_seen_id = get_last_seen_id(gls.value_holder_file)

        mentions = gls.api.mentions_timeline(last_seen_id, tweet_mode='extended')
        # print(mentions[0].__dict__.keys())  # converts list into dict and extracts all the keys
        #
        # print(mentions[0].text)
        # 1163451084704079873 for testing

        for single_mention in reversed(mentions):
            print(f"mention id {single_mention.id} - mention full text {single_mention.full_text}")
            last_seen_id = single_mention.id
            save_last_seen_id(last_seen_id, gls.value_holder_file)

            gls.api.update_status(
                f'this is custom message',
                single_mention.id)

            gls.sleep_time()

    except tweepy.TweepError as ess:
        logging.error('Error occurred ' + str(ess))

    except Exception as eww:
        logging.error('Error occurred ' + str(eww))

    finally:
        pass

    print("custom_replier() has terminated ")


# downloads likes and retweets and saves on a given hashtag
def tweet_list_downloader(downloaded_tweets_csv, hashtag):
    gls.log_file_writer()

    try:
        tweets_csv = open(downloaded_tweets_csv, gls.write)
        csv_writer = csv.writer(tweets_csv)
        print("hashtag downloading on: ", hashtag)
        for single_tweet in tweepy.Cursor(gls.api.search, q=hashtag, rpp=1200, lang="en", since="2018-08-17").items(100000):
            print(single_tweet.id_str)
            single_tweet.favorite()
            gls.sleep_time()
            single_tweet.retweet()

            print(single_tweet.author, single_tweet.created_at, single_tweet.text)

            csv_writer.writerow([str(single_tweet.id_str)+'x', single_tweet.text.encode('utf-8')])

            print("row (hopefully) written into csv")

    except IOError as e2:
        logging.error('Error occurred ' + str(e2))

    except tweepy.TweepError as e3:
        logging.error('Error occurred ' + str(e3))

    except Exception as x4:
        logging.error('Error occurred ' + str(x4))

    finally:
        print("end of like and retweet cycle")


# tweets out images
def image_tweeter(single_image, single_tweet, single_hashtag):
    print("starting image_tweeter()")

    gls.log_file_writer()

    try:
        gls.api.update_with_media(single_image, f"{single_tweet} {single_hashtag}")

        gls.sleep_time()

    except tweepy.TweepError as eu:
        logging.error('Error occurred ' + str(eu))

    finally:
        pass

    print("image_tweeter() has terminated")


# replies to single tweets
def single_tweet_replier(single_tweet_text, tweet_id):
    print("starting single_tweet_replier()")

    gls.log_file_writer()

    try:
        gls.api.update_status(status=single_tweet_text, in_reply_to_status_id=tweet_id[:-1])
        gls.sleep_time()

    except tweepy.TweepError as re:
        logging.error('Error occurred ' + str(re))

    except Exception as et:
        logging.error('Error occurred ' + str(et))

    finally:
        pass

    print("single_tweet_replier() has terminated ")


print("starting with the data downloads...")

my_minion_extractor("minion_and_ids.csv", "awesome1_inc")

for single_account in tweet_source_list:
    tweet_fetcher(single_account)

for single_ht in hashtag_list:
    tweet_list_downloader("tweets_and_ids.csv", single_ht)

for single_source in handle_source_list:
    follower_extractor("follower_and_ids.csv", single_source)

dict_loader()

print(minions_dict)

print("starting with the outbound messages...")

for single_minion_id in minions_dict.keys():
    dm_sender(single_minion_id, "this is test message")


while 1:





