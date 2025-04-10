import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx

st.set_page_config(
    page_title="Global Market Stress Monitor",
    layout="wide"
)

try:
    from dashboard.trading_terminal import show_trading_terminal
    show_trading_terminal()
except Exception as e:
    st.error(f"❌ Failed to load dashboard: {e}")
