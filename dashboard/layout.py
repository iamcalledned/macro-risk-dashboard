import streamlit as st
from data.fetch_fred import get_vix, get_yield_spread, get_dxy
from dashboard.plots import plot_time_series
from data.alerts import check_alerts

def show_dashboard():
    st.title("📉 Macro & Market Conditions Dashboard")

    st.subheader("1. Volatility & Risk Appetite")
    vix_data = get_vix()
    plot_time_series(vix_data, "VIX - Volatility Index", alert_level=25)

    st.subheader("2. Yield Curve: 10Y - 2Y")
    spread_data = get_yield_spread()
    plot_time_series(spread_data, "10Y-2Y Treasury Spread (bps)", alert_level=0)

    st.subheader("3. Dollar Strength")
    dxy_data = get_dxy()
    plot_time_series(dxy_data, "US Dollar Index (DXY)", alert_level=105)

    alerts = check_alerts(vix_data, spread_data, dxy_data)
    if alerts:
        st.markdown("### 🚨 **ALERTS**")
        for alert in alerts:
            st.error(alert)
