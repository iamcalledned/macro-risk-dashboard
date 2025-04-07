import streamlit as st
from dashboard.layout import show_dashboard

st.set_page_config(layout="wide", page_title="Macro Risk Dashboard")
show_dashboard()
