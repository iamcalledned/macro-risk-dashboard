import yfinance as yf
import pandas as pd

def get_btc_usd():
    btc = yf.download("BTC-USD", period="60d", interval="1d")['Close']
    btc.name = "BTC/USD"
    return btc.dropna()
