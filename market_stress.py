import streamlit as st
from data.fetch_fred import get_vix, get_yield_spread, get_dxy
from data.alerts import check_alerts
from dashboard.plots import plot_time_series

def market_stress_tab():
    st.title("🧠 MARKET STRESS DASHBOARD")

    # --- Pull Real Data ---
    with st.spinner("Fetching real-time data..."):
        vix = get_vix().last('60D')
        spread = get_yield_spread().last('60D')
        dxy = get_dxy().last('60D')

    # --- Current Values ---
    st.subheader("📊 Current Readings")
    col1, col2, col3 = st.columns(3)
    col1.metric("VIX", f"{vix.iloc[-1]:.2f}", delta=f"{vix.iloc[-1] - vix.iloc[-2]:.2f}")
    col2.metric("10Y–2Y Spread (bps)", f"{spread.iloc[-1]*100:.2f}", delta=f"{(spread.iloc[-1] - spread.iloc[-2])*100:.2f}")
    col3.metric("DXY", f"{dxy.iloc[-1]:.2f}", delta=f"{dxy.iloc[-1] - dxy.iloc[-2]:.2f}")

    # --- Alerts ---
    for alert in check_alerts(vix, spread, dxy):
        st.error(f"🚨 {alert}")

    # --- Charts ---
    st.subheader("📉 Volatility: VIX")
    plot_time_series(vix, "CBOE VIX", alert_level=25)

    st.subheader("📈 Yield Curve: 10Y–2Y Spread")
    plot_time_series(spread * 100, "10Y–2Y Spread (bps)", alert_level=0)

    st.subheader("💵 USD Strength: DXY Index")
    plot_time_series(dxy, "US Dollar Index (DXY)", alert_level=105)
