#Practical 1: Mining Twitter: Exploring Trending Topics, Discovering What People Are Talking About, and More: Why Is Twitter All the Rage?, Exploring Twitter’s API, Fundamental Twitter Terminology, Creating a Twitter API Connection, Exploring Trending Topics, Searching for Tweets, Analysing Tweets and Tweet Entities with Frequency Analysis.
Roll No.:-				
#Practical1.py import tweepy
#Authenticate to Twitter
Auth=tweepy.OAuthHandler("M42RKxXEWKwj3nlldJvCbJS5Y","UL hQ6WzoaBTpGVG7liGxbwsoQqiFRgh6Lh7SWmh2VqAqDGmhiR")

auth.set_access_token("1757656639291924480- tEVVypc7XoCSRO3mPSc1CbGzxP2aE9","HIEe1Jxoc9ZUX1evsUhmr 9c0s38UbhA8Q87AWrFKc9k3m")
api = tweepy.API(auth) try:
api.verify_credentials()
print("Authentication OK") except:
print("Error during authentication")

# Retrive trending topics for aspecific location(WOEID 1 in this example) trends = api.get_place_trends(1)

# Print the trending topics
for trend in trends[0]['trends']: print(trend['name'])
