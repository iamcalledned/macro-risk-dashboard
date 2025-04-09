import yfinance as yf
import pandas as pd

def get_btc_usd():
    btc = yf.download("BTC-USD", period="60d", interval="1d")['Close']
    btc.name = "BTC/USD"
    return btc.dropna()
import yfinance as yf

def get_sp500():
    spx = yf.download("^GSPC", period="2d", interval="1d")["Close"]
    spx.name = "S&P 500"
    return spx.dropna()
