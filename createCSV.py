import tweepy  # https://github.com/tweepy/tweepy
import csv

# This function is used for downloading about 3200 tweets from a twitter user
# and stores them as a csv file.


# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3000 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]

    # write the csv

    with open('%s_tweets.csv' % screen_name, 'w') as f:
        wrtr = csv.writer(f, delimiter=',', quotechar='"')
        writer = csv.writer(f)
        writer.writerows(outtweets)

    pass

# give the username of the account to download their tweets
get_all_tweets("BarackObama")
