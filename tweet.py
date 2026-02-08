import tweepy
import os
from datetime import date

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

birthday = date(2026, 4, 8)  # Allu Arjun Birthday
today = date.today()
days_left = (birthday - today).days

if days_left > 0:
    tweet = f"{days_left} Days Left For Icon Star @alluarjun's Birthday 🔥"
else:
    tweet = "🎉🎂 It's Icon Star @alluarjun's Birthday 🎂🎉"

client.create_tweet(text=tweet)
