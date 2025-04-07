from fredapi import Fred
import pandas as pd
import os

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

def get_vix():
    data = fred.get_series("VIXCLS").dropna()
    return data

def get_yield_spread():
    ten = fred.get_series("GS10")
    two = fred.get_series("GS2")
    spread = ten - two
    return spread.dropna()

def get_dxy():
    return fred.get_series("DTWEXBGS").dropna()
