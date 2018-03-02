# dependencies
import tweepy
from wordcloud import WordCloud
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# get into twitter API

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, "https://aggiecodingclub.com:2020")

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get desired handle from user

handle = input("Enter twitter name: ")
print("Downloading tweets from " + str(handle))

# put all tweets in a list; code inspired by https://gist.github.com/yanofsky/5436496

all_tweets = []

tweets = api.user_timeline(screen_name = handle, count = 100)
for tweet in tweets:
    all_tweets.append(tweet)

print (str(len(all_tweets)) + " tweets downloaded so far")

while len(tweets) > 0:

    oldest = all_tweets[-1].id - 1
    tweets = api.user_timeline(screen_name = handle, count = 100, max_id = oldest)
    for tweet in tweets:
        all_tweets.append(tweet)
    print (str(len(all_tweets)) + " tweets downloaded so far")

def concatenate(tweets):
    result = ''
    for tweet in tweets:
        words = tweet.text.encode('ascii', 'ignore')
        result += str(words)[2:]
        result += ' '
    return result

text = concatenate(all_tweets)

# generate wordcloud; module found at https://github.com/amueller/word_cloud

print("Generating wordcloud for " + str(handle))
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("tweets")
print("Wordcloud saved")

# tweet wordcloud
status = "@" + handle + "'s wordcloud"
api.update_with_media("tweets.png", status=status)
print("Wordcloud tweeted! Check @wordcloud_fun for results")