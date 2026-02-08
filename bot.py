import tweepy
from datetime import date

# 🔐 Twitter API Credentials (use GitHub Secrets)
API_KEY = "UlRVVOeor8QtiMadRK8Mw3bdI"
API_SECRET = "HnNE6YT6JiIFqDFpzyfk7it7h9K8MUr95egv1apjeLk0e5S0MVYOUR_API_SECRET"
ACCESS_TOKEN = "2012890806584328193-wXwSDaMzv2lcISYeUCtK0OHrznMHKu"
ACCESS_SECRET = "eXJPqDcGnmczbBWLT8a74kTs7gfl82WMssws4MoRd1yFq"

auth = tweepy.OAuth1UserHandler(
    UlRVVOeor8QtiMadRK8Mw3bdI, HnNE6YT6JiIFqDFpzyfk7it7h9K8MUr95egv1apjeLk0e5S0MV, 2012890806584328193-wXwSDaMzv2lcISYeUCtK0OHrznMHKu, eXJPqDcGnmczbBWLT8a74kTs7gfl82WMssws4MoRd1yFq
)
api = tweepy.API(auth)

# 🎂 Allu Arjun Birthday (8 April)
birthday = date(date.today().year, 4, 8)
today = date.today()

days_left = (birthday - today).days

if days_left > 0:
    tweet = (
        f"{days_left} Days Left For Icon Star @alluarjun’s Birthday 🎉🔥\n\n"
        f"Automated by @NorthAlluFans"
    )
elif days_left == 0:
    tweet = (
        "It’s Icon Star @alluarjun’s Birthday 🎂🔥\n\n"
        "Automated by @NorthAlluFans"
    )
else:
    exit()

api.update_status(tweet)
