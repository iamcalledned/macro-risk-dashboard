import streamlit as st
import yfinance as yf

def market_stress_tab():
    st.header("Market Stress")

    # S&P 500
    sp500 = yf.Ticker("^GSPC")
    sp500_data = sp500.history(period="1d", interval="1m")
    st.subheader("S&P 500 Price")
    st.line_chart(sp500_data['Close'])

    # VIX
    vix = yf.Ticker("^VIX")
    vix_data = vix.history(period="1d", interval="1m")
    st.subheader("VIX Index")
    st.line_chart(vix_data['Close'])
