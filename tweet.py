import tweepy
import os
from datetime import date

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET
)
api = tweepy.API(auth)

birthday = date(2026, 4, 8)  # Allu Arjun Birthday
today = date.today()
days_left = (birthday - today).days

if days_left > 0:
    tweet = f"{days_left} Days Left For Icon Star @alluarjun's Birthday 🔥"
else:
    tweet = "🎉🎂 It's Icon Star @alluarjun's Birthday 🎂🎉"

api.update_status(tweet)
