from ntscraper import Nitter
#initialize
scraper = Nitter(log_level=1, skip_instance_check=False)
#Scrape tweets
terms = ["github", "bezos", "musk"]

results = scraper.get_tweets(terms, mode='term')
#multi processing
terms = ["github", "bezos", "musk"]

results = scraper.get_tweets(terms, mode='term')

#get single tweet:
tweet = scraper.get_tweet_by_id("x", "1826317783430303888")

#get profile information:
bezos_information = scraper.get_profile_info("JeffBezos")

#multi processing
usernames = ["x", "github"]

results = scraper.get_profile_info(usernames)