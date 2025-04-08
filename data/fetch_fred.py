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

def get_fed_funds():
    data = fred.get_series("FEDFUNDS").dropna()
    data.name = "Fed Funds Rate"
    return data

def get_cpi_yoy():
    data = fred.get_series("CPALTT01USM657N").dropna()
    data.name = "CPI YoY"
    return data

def get_5y5y_breakeven():
    data = fred.get_series("T5YIFR").dropna()
    data.name = "5Y5Y Inflation Breakeven"
    return data

def get_sofr():
    data = fred.get_series("SOFR").dropna()
    data.name = "SOFR Rate"
    return data

def get_10y3m_spread():
    ten = fred.get_series("GS10")
    three = fred.get_series("TB3MS")
    spread = ten - three
    spread.name = "10Y–3M Spread"
    return spread.dropna()

def get_10y2y_spread():
    ten = fred.get_series("GS10")
    two = fred.get_series("GS2")
    spread = ten - two
    spread.name = "10Y–2Y Spread"
    return spread.dropna()

def get_consumer_credit():
    data = fred.get_series("TOTALSL").dropna()
    data.name = "Consumer Credit Total"
    return data

def get_nonrevolving_credit():
    data = fred.get_series("NONREVSL").dropna()
    data.name = "Non-Revolving Credit"
    return data

def get_auto_loan_rate():
    data = fred.get_series("TERMCBAUTO48NS").dropna()
    data.name = "Auto Loan 60-Month Rate"
    return data

def get_baml_hy():
    data = fred.get_series("BAMLH0A0HYM2").dropna()
    data.name = "BAML HY OAS"
    return data

def get_baml_ig():
    data = fred.get_series("BAMLC0A0CM").dropna()
    data.name = "BAML IG OAS"
    return data

def get_sofr():
    data = fred.get_series("SOFR").dropna()
    data.name = "SOFR"
    return data

def get_wti():
    data = fred.get_series("DCOILWTICO").dropna()
    data.name = "WTI Crude"
    return data

def get_gasoline():
    data = fred.get_series("GASREGCOVW").dropna()
    data.name = "Gasoline"
    return data

def get_gold():
    data = fred.get_series("IR14270").dropna()
    data.name = "Gold (USD/oz)"
    return data
def get_em_fx():
    """Trade-Weighted USD Index vs EM FX (FRED Proxy)"""
    data = fred.get_series("DTWEXEMEGS").dropna()
    data.name = "USD vs EM FX (TW)"
    return data

def get_china_loans_yoy():
    """Proxy for China Credit Impulse — China Bank Loans YoY Growth"""
    data = fred.get_series("CHNBLYOY").dropna()
    data.name = "China Loan Growth YoY"
    return data
def get_china_industrial_prod():
    """China Industrial Production YoY (%)"""
    data = fred.get_series("IPMAN").dropna()
    data.name = "China Industrial Production YoY"
    return data
