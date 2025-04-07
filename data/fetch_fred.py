from fredapi import Fred
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get FRED API key from environment
api_key = os.getenv("FRED_API_KEY")
if not api_key:
    raise ValueError("FRED_API_KEY not found in environment. Make sure it's set in your .env file.")

# Create Fred instance
fred = Fred(api_key=api_key)

def get_vix():
    """CBOE Volatility Index (VIX)"""
    data = fred.get_series("VIXCLS").dropna()
    data.name = "VIX"
    return data

def get_yield_spread():
    """10-Year minus 2-Year Treasury spread (in % points)"""
    ten = fred.get_series("GS10")
    two = fred.get_series("GS2")
    spread = ten - two
    spread.name = "10Y-2Y Spread"
    return spread.dropna()

def get_dxy():
    """US Dollar Index (Broad Dollar Index)"""
    data = fred.get_series("DTWEXBGS").dropna()
    data.name = "DXY"
    return data
