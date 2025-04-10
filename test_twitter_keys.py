import os
import requests
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def test_twitter_api():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    # Test: search for recent tweets about the S&P 500 ETF
    params = {
        "query": "SPY -is:retweet lang:en",
        "max_results": 10
    }

    url = "https://api.twitter.com/2/tweets/search/recent"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("✅ Twitter API connection successful.")
        tweets = response.json().get("data", [])
        for tweet in tweets:
            print("-", tweet["text"])
    else:
        print("❌ Failed to connect to Twitter API")
        print("Status:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    test_twitter_api()
