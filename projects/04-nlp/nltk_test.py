import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got
from sys import argv

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# python3 nltk_test.py "london" 1000 "2020-05-12" "2020-05-12"

search_query = argv[1]
number_of_tweets = argv[2]
start_date = argv[3]
end_date = argv[4]

print(search_query,number_of_tweets,start_date,end_date)

tweet_list = []
final_words = []

# get sentiment score as list
def get_sentiment_score_list(text):
    score_list = SentimentIntensityAnalyzer().polarity_scores(text)
    return score_list

# Get data from Twitter based on search query and store in data.txt file
def get_tweets(query,limit,from_date,to_date):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince(from_date)\
                                           .setUntil(to_date)\
                                           .setMaxTweets(int(limit))
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    for tweet in tweets:
        tweet_list.append(tweet.text)

    return tweet_list
    

tweets = get_tweets(search_query,number_of_tweets,start_date,end_date)

tweet_text = '\n'.join(tweets)

with open("data.txt","w") as data_file:
    data_file.write(tweet_text)
    
# Clean the data by removing punctuation and making all letters to lower letters

lower_case_text = open("data.txt", "r", encoding="utf-8").read().lower()
# ASCII value - setting all punctuation characters to none
clean_text = lower_case_text.translate(
    str.maketrans("", "", string.punctuation))

# get sentiment score
score = get_sentiment_score_list(clean_text)
#print(score)

if score["neg"] > score["pos"]:
    print(search_query + " - Overall Negative vibes")
elif score["neg"] < score["pos"]:
    print(search_query + " - Overall Positive vibes")
elif score["neg"] == score["pos"]:
    print(search_query + " - Overall Neutral vibes")

# Tokenize the text using NLTK
words_list = word_tokenize(clean_text)

#print("coming to clean text")
# remove meaningless words from text
for word in words_list:
    if word not in stopwords.words():
        final_words.append(word)
#print("Finished clean text")

#print(final_words)
emotion_list = []

#print("coming to add emotion")
with open("emotions.txt","r") as f:
    for line in f:
        word, emotion = line.replace("\n","").replace("'","").replace(",","").split(":")

        #print(word + " - Emotion - "+ emotion)
        if word in final_words:
            emotion_list.append(emotion)
#print("Finished add emotion")
emotion_counter =  Counter(emotion_list)
#print(emotion_counter)

fig, ax = plt.subplots()
ax.bar(emotion_counter.keys(),emotion_counter.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()