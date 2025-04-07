from fredapi import Fred
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 Load variables from .env

fred = Fred(api_key=os.getenv("FRED_API_KEY"))
