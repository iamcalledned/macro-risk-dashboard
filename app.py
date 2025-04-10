import streamlit as st

# Must come BEFORE any other Streamlit command
st.set_page_config(
    layout="wide",
    page_title="Global Market Stress Monitor"
)

# Import all dashboard views
from pages.overview import show_main_dashboard
from pages.market_stress import market_stress_tab
from pages.credit_liquidity import credit_liquidity_tab
from pages.macro_fed_watch import macro_fed_watch_tab
from pages.global_panic import global_panic_tab
from pages.recession_confirmation import recession_confirmation_tab
from dashboard.trading_terminal import show_trading_terminal  # ✅ NEW

# Render sidebar navigation
tab = st.sidebar.radio("Select a Dashboard", [
    "Overview",
    "Market Stress",
    "Credit & Liquidity",
    "Macro & Fed Watch",
    "Global Panic Indicators",
    "Recession Confirmation",
    "Trading Terminal"  # ✅ NEW
])

# Route to the appropriate tab
if tab == "Overview":
    show_main_dashboard()
elif tab == "Market Stress":
    market_stress_tab()
elif tab == "Credit & Liquidity":
    credit_liquidity_tab()
elif tab == "Macro & Fed Watch":
    macro_fed_watch_tab()
elif tab == "Global Panic Indicators":
    global_panic_tab()
elif tab == "Recession Confirmation":
    recession_confirmation_tab()
elif tab == "Trading Terminal":
    show_trading_terminal()
