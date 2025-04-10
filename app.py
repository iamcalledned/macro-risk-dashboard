import streamlit as st
from dashboard.trading_terminal import show_trading_terminal

st.set_page_config(
    page_title="Global Market Stress Monitor",
    layout="wide"
)

show_trading_terminal()
