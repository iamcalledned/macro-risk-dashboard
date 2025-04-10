import yfinance as yf
import pandas as pd

def get_btc_usd():
    btc = yf.download("BTC-USD", period="60d", interval="1d")['Close']
    btc.name = "BTC/USD"
    return btc.dropna()


def get_sp500():
    df = yf.download("^GSPC", period="2d", interval="1d")
    if "Close" in df.columns:
        return df["Close"].dropna()
    else:
        return pd.Series(dtype=float)