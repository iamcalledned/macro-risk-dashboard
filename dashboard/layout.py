import streamlit as st
import pandas as pd
import numpy as np

def fake_timeseries(title, days=60):
    dates = pd.date_range(end=pd.Timestamp.today(), periods=days)
    data = np.cumsum(np.random.randn(days)) + 100
    return pd.DataFrame({title: data}, index=dates)

def show_dashboard():
    st.title("📊 Global Market Stress Monitor")

    tabs = st.tabs([
        "Market Stress",
        "Credit & Liquidity",
        "Macro & Fed Watch",
        "Global Panic Indicators",
        "Recession Confirmation"
    ])

    with tabs[0]:
        st.header("📉 Market Stress")
        st.line_chart(fake_timeseries("S&P 500"))
        st.line_chart(fake_timeseries("VIX Index"))
        st.line_chart(fake_timeseries("Put/Call Ratio"))
        st.line_chart(fake_timeseries("Advance/Decline"))

    with tabs[1]:
        st.header("💳 Credit & Liquidity")
        st.line_chart(fake_timeseries("CDX IG"))
        st.line_chart(fake_timeseries("CDX HY"))
        st.metric("HY-IG Spread Delta", value="87bps", delta="+4bps")
        st.line_chart(fake_timeseries("SOFR 3Y Spread"))
        st.line_chart(fake_timeseries("EUR/USD Cross Basis"))
        st.line_chart(fake_timeseries("GS RAI"))

    with tabs[2]:
        st.header("🏦 Macro & Fed Watch")
        st.line_chart(fake_timeseries("Fed Funds 1Y Forward"))
        st.line_chart(fake_timeseries("10Y - 2Y Spread"))
        st.line_chart(fake_timeseries("5Y5Y Inflation"))
        st.bar_chart(np.random.rand(5))  # Placeholder sentiment bar
        st.metric("CPI YoY", value="3.6%", delta="-0.1%")

    with tabs[3]:
        st.header("🌎 Global Panic Indicators")
        st.line_chart(fake_timeseries("DXY"))
        st.line_chart(fake_timeseries("EM FX"))
        st.line_chart(fake_timeseries("China Credit Impulse"))
        st.line_chart(fake_timeseries("Gasoline Prices"))
        st.line_chart(fake_timeseries("Gold & BTC"))

    with tabs[4]:
        st.header("⚠️ Recession Confirmation")
        st.line_chart(fake_timeseries("Consumer Credit"))
        st.line_chart(fake_timeseries("Non-Revolving Credit"))
        st.bar_chart(np.random.rand(7))  # Placeholder loan rates
        st.text("📅 Macro Shock Timeline (placeholder)")
