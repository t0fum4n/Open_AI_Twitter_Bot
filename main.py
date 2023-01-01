import openai
import tweepy
import config

# Set up the Tweepy API client with your access keys and secrets
client = tweepy.Client(consumer_key=config.ck,
                       consumer_secret= config.cs,
                       access_token=config.at,
                       access_token_secret=config.ats)

# Configure the openai module by setting the secret key

openai.api_key = config.oik

# Open a file named input.txt and read that entire file into a variable named input

with open('tweetrequest.txt') as t:
    tweetrequest = t.read()

# Print the value of the variable named input

print(tweetrequest)

# create a completion

response = openai.Completion.create(

    model="text-davinci-003",

    max_tokens=500,

    prompt=tweetrequest,

    temperature=0.9,

    top_p=1,

    stop="|<EndOfText>|")

# Write the generated text to the tweet.txt file

#with open("tweet.txt", "w") as f:
#    f.write(response.choices[0].text)

# print the completion

print(response.choices[0].text)

# Post response as tweet

response = client.create_tweet(text=response.choices[0].text)
