import streamlit as st
from data.fetch_fred import get_baml_hy, get_baml_ig, get_sofr
from dashboard.plots import plot_time_series
from datetime import datetime

def credit_liquidity_tab():
    st.markdown("## 💳 Credit & Liquidity Dashboard")

    # --- Load Real Data ---
    with st.spinner("Fetching real-time data..."):
        hy = get_baml_hy().last('60D')
        ig = get_baml_ig().last('60D')
        hy_ig_spread = (hy - ig)
        sofr = get_sofr().last('60D')
        last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # --- Display Metrics ---
    st.markdown("### 📊 Current Market Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("BAML HY OAS", f"{hy.iloc[-1]:.1f} bps")
    col2.metric("BAML IG OAS", f"{ig.iloc[-1]:.1f} bps")
    col3.metric("HY - IG Spread", f"{hy_ig_spread.iloc[-1]:.1f} bps")

    col4, _ = st.columns(2)
    col4.metric("💧 SOFR", f"{sofr.iloc[-1]:.2f}%")

    st.caption(f"🔄 Data last updated: {last_updated}")

    # --- Alerts ---
    st.markdown("---")
    st.markdown("### 🚨 Alerts")
    if hy_ig_spread.iloc[-1] > 300:
        st.warning("High yield–IG spread exceeds 300bps — potential risk-off signal.")
    if sofr.iloc[-1] > 6:
        st.error("SOFR above 6% — funding market pressure.")

    # --- Charts Section ---
    st.markdown("---")
    st.markdown("### 📈 Trend Breakdown")
    with st.expander("📉 Credit Spreads: BAML HY vs IG"):
        plot_time_series(hy.to_frame().join(ig), "BAML High Yield vs Investment Grade OAS")

    with st.expander("📊 HY - IG Spread"):
        plot_time_series(hy_ig_spread, "HY – IG Spread (bps)", alert_level=300)

    with st.expander("💧 SOFR Rate"):
        plot_time_series(sofr, "Secured Overnight Financing Rate (SOFR)", alert_level=6.0)
