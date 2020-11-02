import tweepy

def getKey():
    with open('apiKey.txt') as f:
        lines = [line.rstrip() for line in f]
    return lines

def request():
    keys = getKey() #set keys to return of getKey()
    userID= 'realDonaldTrump'
    consumer_key = keys[0]#Setting sensitive and secret keys from 'keys'
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)#setting up all the authentication
    auth.set_access_token(access_token, access_token_secret)#setting up authentication
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=userID, #Collecting 200 tweets from the API
    count=200, include_rts= False, tweet_mode= 'extended')
    return tweets

def getTweets():
    data = request() #Set data to return of request() 'tweets'
    Tweets = []#Create list to hold tweets
    for info in data:#cycle through data and 
        Tweets.append(info.full_text)#Append only the full_text(tweet text)
    #print(Tweets)
    for tweet in Tweets:
        print(tweet,'\n')#Print Tweets out
    return Tweets

getTweets()