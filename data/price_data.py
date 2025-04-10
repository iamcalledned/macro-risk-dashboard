import requests
import pandas as pd
from datetime import datetime

TWELVE_DATA_API_KEY = "YOUR_API_KEY_HERE"

def get_intraday_prices(symbol="SPY", interval="1min", outputsize=60):
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": TWELVE_DATA_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "values" not in data:
        raise ValueError(f"Error from Twelve Data: {data.get('message', 'Unknown error')}")

    df = pd.DataFrame(data["values"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["price"] = df["close"].astype(float)
    df = df.sort_values("datetime")

    return df[["datetime", "price"]]
