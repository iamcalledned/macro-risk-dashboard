import streamlit as st
from market_stress import market_stress_tab
from credit_liquidity import credit_liquidity_tab
from macro_fed_watch import macro_fed_watch_tab
from global_panic import global_panic_tab
from recession_confirmation import recession_confirmation_tab

st.set_page_config(layout="wide", page_title="Global Market Stress Monitor")

TABS = {
    "Market Stress": market_stress_tab,
    "Credit & Liquidity": credit_liquidity_tab,
    "Macro & Fed Watch": macro_fed_watch_tab,
    "Global Panic Indicators": global_panic_tab,
    "Recession Confirmation": recession_confirmation_tab,
}

selected_tab = st.sidebar.radio("Select Dashboard Tab", list(TABS.keys()))
TABS[selected_tab]()
