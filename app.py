import streamlit as st
from dashboard.overview import show_main_dashboard

tab = st.sidebar.radio("Select a Dashboard", [
    "Overview",
    "Market Stress",
    "Credit & Liquidity",
    "Macro & Fed Watch",
    "Global Panic Indicators",
    "Recession Confirmation"
])

if tab == "Overview":
    show_main_dashboard()
# (rest stays the same)


# Must come BEFORE any other Streamlit command
st.set_page_config(
    layout="wide",
    page_title="Global Market Stress Monitor"
)

# Now safe to import the rest
from market_stress import market_stress_tab
from credit_liquidity import credit_liquidity_tab
from macro_fed_watch import macro_fed_watch_tab
from global_panic import global_panic_tab
from recession_confirmation import recession_confirmation_tab

# Render navigation
tab = st.sidebar.radio("Select a Dashboard", [
    "Market Stress",
    "Credit & Liquidity",
    "Macro & Fed Watch",
    "Global Panic Indicators",
    "Recession Confirmation"
])

if tab == "Market Stress":
    market_stress_tab()
elif tab == "Credit & Liquidity":
    credit_liquidity_tab()
elif tab == "Macro & Fed Watch":
    macro_fed_watch_tab()
elif tab == "Global Panic Indicators":
    global_panic_tab()
elif tab == "Recession Confirmation":
    recession_confirmation_tab()
