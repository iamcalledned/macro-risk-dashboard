import streamlit as st
from data.fetch_fred import get_baml_hy, get_baml_ig, get_sofr
from dashboard.plots import plot_time_series

def credit_liquidity_tab():
    st.header("💳 Credit & Liquidity Dashboard")

    # --- Load Real Data ---
    hy = get_baml_hy().last('60D')
    ig = get_baml_ig().last('60D')
    hy_ig_spread = (hy - ig)
    sofr = get_sofr().last('60D')

    # --- Display Current Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("BAML HY OAS", f"{hy.iloc[-1]:.1f} bps")
    col2.metric("BAML IG OAS", f"{ig.iloc[-1]:.1f} bps")
    col3.metric("HY - IG Spread", f"{hy_ig_spread.iloc[-1]:.1f} bps")

    col4, _ = st.columns(2)
    col4.metric("SOFR", f"{sofr.iloc[-1]:.2f}%")

    # --- Alerts ---
    if hy_ig_spread.iloc[-1] > 300:
        st.warning("🚨 HY–IG spread exceeds 300bps — high credit risk signal.")
    if sofr.iloc[-1] > 6:
        st.error("⚠️ SOFR is elevated (>6%) — funding stress potential.")

    # --- Charts ---
    st.subheader("📉 Credit Spreads: BAML HY vs IG")
    plot_time_series(hy.to_frame().join(ig), "BAML High Yield vs Investment Grade OAS")

    st.subheader("📊 HY - IG Spread")
    plot_time_series(hy_ig_spread, "HY – IG Spread (bps)", alert_level=300)

    st.subheader("💧 SOFR Rate")
    plot_time_series(sofr, "Secured Overnight Financing Rate (SOFR)", alert_level=6.0)
