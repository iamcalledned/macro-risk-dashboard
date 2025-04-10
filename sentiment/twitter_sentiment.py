import os
import requests
from dotenv import load_dotenv
from textblob import TextBlob
import pandas as pd
from datetime import datetime

# Load Twitter API key
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def fetch_recent_tweets(query="SPY", max_results=30):
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": f"{query} -is:retweet lang:en",
        "max_results": max_results,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Twitter API error: {response.status_code} - {response.text}")
    return response.json().get("data", [])

def analyze_sentiment(tweets):
    results = []
    for tweet in tweets:
        text = tweet["text"]
        blob = TextBlob(text)
        score = blob.sentiment.polarity  # -1 to 1
        results.append({
            "text": text,
            "score": score,
            "timestamp": datetime.utcnow()
        })
    return results

def get_sentiment_dataframe(query="SPY"):
    tweets = fetch_recent_tweets(query)
    analyzed = analyze_sentiment(tweets)
    df = pd.DataFrame(analyzed)
    return df
