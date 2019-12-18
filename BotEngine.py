import tweepy
import globals as gls
import csv
import logging
import glob

print("starting my engines...")

my_minion_list = []
minion_id_list = []
custom_tweet_list = []
custom_handle_list = []
follower_list = []
follower_id_list = []
handle_source_list = ["FactSoup",
                      "Casey",
                      "ithinkthatway"
                      ]
tweet_source_list = ["FactSoup",
                     "Fact",
                     "SmiIe",
                     "ithinkthatway"]
image_list = glob.glob("media/*")

first_line = True
try:
    with open(gls.tweets_csv, gls.read) as rdr:
        reader = csv.reader(rdr, delimiter=",")
        for single_row in reader:
            if first_line:  # this skips th first line
                first_line = False
                continue  # used this way, the rest of the code from here is skipped in this loop

            custom_tweet_list.append(single_row)

except IOError as x:
    print("problem reading the csv")
    logging.error('Error occurred ' + str(x))
except Exception as e:
    print("the problem is: ", e)
    logging.error('Error occurred ' + str(e))

finally:
    pass


# saves tweets into file
def save_downloaded_tweets(tweet_list, my_file):
    f_write = open(my_file, gls.write)
    for single_tweet in tweet_list:
        try:
            f_write.write(str(single_tweet))
            f_write.write("\n")
        except Exception as ex:
            print("the issue is: ", e)
            logging.error('Error occurred ' + str(ex))
        finally:
            f_write.close()
    return


# reads tweets as list
def read_downloaded_tweets(my_file):
    downloaded_tweets = []
    f_read = open(my_file, gls.read)
    try:
        downloaded_tweets = f_read.readlines()
    except Exception as ep:
        print("problem reading list, ", ep)
        logging.error('Error occurred ' + str(ep))
    finally:
        f_read.close()
    return downloaded_tweets


# saves handles into a file
def save_downloaded_handles(handle_list, my_file):
    f_write = open(my_file, gls.write)
    for single_handle in handle_list:
        try:
            f_write.write(str(single_handle))
            f_write.write(str("\n"))
        except Exception as e1:
            print("the problem is, ", e1)
            logging.error('Error occurred ' + str(e1))

        finally:
            f_write.close()
    return


# reads handles into a file
def read_saved_handles(my_file):
    handles = []
    f_read = open(my_file, gls.read)
    try:
        handles = f_read.readlines()
    except Exception as ep:
        print("problem reading handles list, ", ep)
        logging.error('Error occurred ' + str(ep))
    finally:
        f_read.close()
    return handles


# gets a list of all followers from a given user
def follower_extractor(single_handle):
    print(" follower_extractor() starting...")
    gls.log_file_writer()
    try:
        for single_follower in tweepy.Cursor(gls.api.followers, screen_name=single_handle).items():
            print(f"{single_follower.id} - {single_follower.screen_name}")
            follower_list.append(single_follower.screen_name)
            follower_id_list.append(single_follower.id)
            break

    except tweepy.TweepError as em:
        logging.error('Error occurred ' + str(em))

    finally:
        pass

    print("len of follower id list ", len(follower_id_list))
    print("len of handle list ", len(follower_list))


# extracts all tweets of a given user
def tweet_fetcher(screen_name):
    print(" tweet_fetcher() starting...")

    # initialize a list to hold all the tweepy Tweets
    all_tweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = gls.api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    all_tweets.extend(new_tweets)

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
    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(out_tweets)

    pass


# this loop gets a list of everyone i follow
def minion_extractor(self):
    print(" minion_extractor() starting...")
    gls.log_file_writer()
    try:
        for single_follower in tweepy.Cursor(gls.api.followers, screen_name="awesome1_inc").items():
            print(f"{single_follower.id} - {single_follower.screen_name}")
            my_minion_list.append(single_follower.screen_name)
            minion_id_list.append(single_follower.id)

    except tweepy.TweepError as ev:
        logging.error('Error occurred ' + str(ev))

    finally:
        pass

    print("len of follower id list ", len(self.follower_id_list))
    print("len of handle list ", len(self.screen_name_list))


# only sends dms to people that follow me
def dm_sender(minion_id, text):
    print("starting dm_sender()")

    gls.log_file_writer()
    try:
        gls.api.send_direct_message(minion_id, text)

    except tweepy.TweepError as ue:
        logging.error('Error occurred ' + str(ue))

    except Exception as ep:
        logging.error('Error occurred ' + str(ep))

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

    finally:
        pass

    print("tweet_sender() has terminated")


def twitter_user_follower(single_handle):
    print("starting twitter_user_follower()")

    gls.log_file_writer()
    try:

        print(f"creating friendship with: {single_handle}")

        gls.api.create_friendship(screen_name=single_handle)

        gls.sleep_time()

    except tweepy.TweepError as ef:
        logging.error('Error occurred ' + str(ef))

    except Exception as eg:
        logging.error('Error occurred ' + str(eg))

    finally:
        pass

    print("twitter_user_follower() has terminated")


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


# downloads likes and retweets and saves om a given hashtag
def tweet_list_downloader(downloaded_tweets_csv, hashtag):
    gls.log_file_writer()

    try:
        tweets_csv = open(downloaded_tweets_csv, "w")
        csv_writer = csv.writer(tweets_csv)
        print("hashtag downloading on: ", hashtag)
        for single_tweet in tweepy.Cursor(gls.api.search, q=hashtag, rpp=1200, lang="en", since="'2018-08-17'").items(1000):
            print(single_tweet.id_str)
            single_tweet.favorite()
            gls.sleep_time()
            single_tweet.retweet()
            gls.sleep_time()

            print(single_tweet.author, single_tweet.created_at, single_tweet.text)

            csv_writer.writerow([str(single_tweet.id_str) + "x", single_tweet.text.encode('utf-8')])

            print("row (hopefully )written into csv")

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


def single_tweet_replier(single_tweet, tweet_id):
    print("starting single_tweet_replier()")

    gls.log_file_writer()

    try:
        gls.api.update_status(status=single_tweet, in_reply_to_status_id=tweet_id[:-1])
        gls.sleep_time()

    except tweepy.TweepError as re:
        logging.error('Error occurred ' + str(re))

    except Exception as et:
        logging.error('Error occurred ' + str(et))

    finally:
        pass

    print("single_tweet_replier() has terminated ")
