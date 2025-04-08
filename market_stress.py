import streamlit as st
import pandas as pd
import numpy as np
import datetime

def generate_dummy_data(name, days=30, base=100, volatility=5):
    dates = pd.date_range(end=datetime.datetime.today(), periods=days)
    data = base + np.cumsum(np.random.randn(days) * volatility)
    return pd.DataFrame({name: data}, index=dates)

def market_stress_tab():
    st.title("🧠 MARKET STRESS DASHBOARD")

    st.subheader("📉 Credit Spread Watch: CDX HY vs IG")
    cdx_ig = generate_dummy_data("CDX IG", base=80, volatility=1)
    cdx_hy = generate_dummy_data("CDX HY", base=400, volatility=10)
    credit_spreads = pd.concat([cdx_ig, cdx_hy], axis=1)
    st.line_chart(credit_spreads)
    if cdx_hy.iloc[-1, 0] > 500:
        st.warning("🚨 High Yield Spread > 500bps — Credit stress alarm!")

    st.subheader("📊 Cross-Asset Volatility: MOVE vs VIX")
    move = generate_dummy_data("MOVE", base=120, volatility=5)
    vix = generate_dummy_data("VIX", base=20, volatility=3)
    volatility_combo = pd.concat([move, vix], axis=1)
    st.line_chart(volatility_combo)
    if move.iloc[-1, 0] > 160 and vix.iloc[-1, 0] > 40:
        st.error("🔥 MOVE > 160 and VIX > 40 — full-on panic mode!")

    st.subheader("💧 Treasury Market Liquidity: Swap Spreads & SPX Liquidity")
    swap_spread = generate_dummy_data("3Y SOFR Swap Spread", base=-10, volatility=3)
    st.line_chart(swap_spread)
    spx_liquidity = np.random.uniform(1_000_000, 5_000_000)
    st.metric("SPX Top-of-Book Liquidity", f"${spx_liquidity:,.0f}/side")
    if swap_spread.iloc[-1, 0] < -30:
        st.warning("🚿 Swap spread < -30bps — treasury stress showing.")
    if spx_liquidity < 3_000_000:
        st.warning("🪙 SPX liquidity < $3M/side — shallow books, be careful.")

    st.subheader("🔻 Risk Appetite Indicator (RAI)")
    rai_value = np.random.normal(loc=-1.5, scale=0.5)
    st.metric("GS Risk Appetite Indicator", f"{rai_value:.2f}")
    if rai_value < -2:
        st.info("🔻 RAI < -2 — historic dip zone. Eye on reversals.")

    st.subheader("🧨 Explosive Headline Sensitivity Index")
    st.markdown("Measuring market fragility to headlines using intraday futures volatility.")
    headline_trigger = np.random.choice([True, False], p=[0.2, 0.8])
    if headline_trigger:
        st.error("💥 Headline Detonator Detected — Risk levels unstable.")
    else:
        st.success("Market stable — no headline detonator activity detected.")
