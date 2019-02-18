from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)

consumerkey="ELzyulnKGDLvAW8gBMC3HChK3"
consumerSecret="5hufnyMjLf5cQGWYznJvD4tNFiEMIP9C4UFxNcKNBvlhmdS1He"
accessToken="1045251215649427456-teNEU2MVXl5rNJG0adOoODI63YfkSt"
accessTokenSecret="gp7274xZL0MmJi8HTS2Kmh1h9UuJZAVSPY43rgkPF1L4U"


auth=tweepy.OAuthHandler(consumer_key=consumerkey,consumer_secret=consumerSecret)
auth.set_access_token (accessToken, accessTokenSecret)
api=tweepy.API(auth)

searchTerm=input("Enter keyword/hashtag to search:-")
noOfSearchTerms=int(input("Enter how many tweets to be analyze:-"))
#tweets = tweepy.Cursor(api.search, q=searchTerm, count=100, lang="en").items(noOfSearchTerms)
tweets = tweepy.Cursor(api.search, q=searchTerm,count=1000, lang="en").items(noOfSearchTerms)



positive = 0.00
negative = 0.00
neutral = 0.00
polarity = 0.00


for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    #print("printing polarity"+str(polarity))

    if(analysis.sentiment.polarity == 0):
        neutral += 1

    elif(analysis.sentiment.polarity < 0):
        negative += 1
    elif(analysis.sentiment.polarity > 0):
        positive += 1
        #print(tweet.text)
        #print("printing polarity " + str(polarity))


positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

print("How people are reacting on " +searchTerm+ " by analysing "+str(noOfSearchTerms)+" tweets")


#if(polarity == 0.00):
#    print("Neutral")
#elif(polarity < 0.00):
 #   print("Negative")
#elif(polarity > 0.00):
 #   print("positive")



print("positive= "+positive+"%")
print("nagetive= "+negative+"%")
print("neutral= "+neutral+"%")
if(positive > negative) and (positive > neutral):
    print("Opinion of people on Twitter about "+searchTerm+" is Positive")
elif(negative > positive) and (negative > neutral):
    print("Opinion of people on Twitter about "+searchTerm+" is Negative")
else:
    print("Opinion of people on Twitter about "+searchTerm+" is Neutral")




labels = ['Positive['+str(positive)+'%]','Negative['+str(negative)+'%]','Neutral['+str(neutral)+'%]' ]
sizes = [positive, negative, neutral]
color = ['blue', 'yellow', 'pink']
patches, texts = plt.pie(sizes, colors=color, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analysing '+str(noOfSearchTerms)+' tweets')
plt.axis ('equal')
plt.tight_layout()
plt.show()




