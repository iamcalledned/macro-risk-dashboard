import streamlit as st

# ✅ This must be FIRST before anything else Streamlit
st.set_page_config(layout="wide", page_title="Global Market Stress Monitor")

from dashboard.layout import show_dashboard

show_dashboard()
