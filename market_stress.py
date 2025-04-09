import streamlit as st
from data.fetch_fred import get_vix, get_yield_spread, get_dxy
from data.alerts import check_alerts
from dashboard.plots import plot_time_series
from datetime import datetime

def market_stress_tab():
    st.markdown("## 🧠 Market Stress Dashboard")

    with st.spinner("Fetching real-time data..."):
        vix = get_vix().last('60D')
        spread = get_yield_spread().last('60D')
        dxy = get_dxy().last('60D')
        last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # --- Header metrics ---
    st.markdown("### 📊 Current Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("VIX", f"{vix.iloc[-1]:.2f}", f"{vix.iloc[-1] - vix.iloc[-2]:+.2f}")
    col2.metric("10Y–2Y Spread (bps)", f"{spread.iloc[-1]*100:.2f}", f"{(spread.iloc[-1] - spread.iloc[-2])*100:.2f}")
    col3.metric("DXY", f"{dxy.iloc[-1]:.2f}", f"{dxy.iloc[-1] - dxy.iloc[-2]:+.2f}")

    st.caption(f"🔄 Data last updated: {last_updated}")

    # --- Alerts ---
    alerts = check_alerts(vix, spread, dxy)
    if alerts:
        st.warning("🚨 Alerts:")
        for alert in alerts:
            st.error(f"• {alert}")
    else:
        st.success("✅ No alerts triggered.")

    # --- Charts Section ---
    with st.container():
        st.markdown("---")
        st.markdown("### 🔍 Trend Breakdown")
        
        with st.expander("📉 Volatility: VIX"):
            plot_time_series(vix, "CBOE VIX", alert_level=25)
        
        with st.expander("📈 Yield Curve: 10Y–2Y Spread"):
            plot_time_series(spread * 100, "10Y–2Y Spread (bps)", alert_level=0)
        
        with st.expander("💵 USD Strength: DXY Index"):
            plot_time_series(dxy, "US Dollar Index (DXY)", alert_level=105)
