import GetOldTweets3 as got
from sys import argv
import string
from collections import Counter
import matplotlib.pyplot as plt

search_query = argv[1]
tweet_list = []

def get_tweets(query):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince("2020-05-01")\
                                           .setUntil("2020-05-12")\
                                           .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    for tweet in tweets:
        tweet_list.append(tweet.text)

    return tweet_list
    

tweets = get_tweets(search_query)

tweet_text = '\n'.join(tweets)

with open("data.txt","w") as data_file:
    data_file.write(tweet_text)

lower_case_text = tweet_text.lower()
# ASCII value - setting all punctuation characters to none
clean_text = lower_case_text.translate(
    str.maketrans("", "", string.punctuation))

words_list = clean_text.split()

useless_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself","yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself","they", "them", "their", "theirs","themselves", "what", "which", "who", "whom", "this", "that", "these","those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do","does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while","of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before","after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again","further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each","few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than","too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in words_list:
    if word not in useless_words:
        final_words.append(word)

#print(final_words)
emotion_list = []

with open("emotions.txt","r") as f:
    for line in f:
        word, emotion = line.replace("\n","").replace("'","").replace(",","").split(":")

        #print(word + " - Emotion - "+ emotion)
        if word in final_words:
            print(word)
            emotion_list.append(emotion)

emotion_counter =  Counter(emotion_list)
print(emotion_counter)

fig, ax = plt.subplots()
ax.bar(emotion_counter.keys(),emotion_counter.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()