import streamlit as st
from data.fetch_fred import get_dxy, get_wti, get_gasoline, get_gold
from dashboard.plots import plot_time_series
import pandas as pd
import numpy as np

def global_panic_tab():
    st.header("🌎 Global Panic Indicators")

    # Fetch data
    dxy = get_dxy().last('60D')
    wti = get_wti().last('60D')
    gas = get_gasoline().last('60D')
    gold = get_gold().last('60D')

    # Simulated placeholders
    em_fx = pd.Series(np.cumsum(np.random.randn(60)) + 100, 
                      index=dxy.index, name="EM FX Index (Simulated)")
    china_credit = pd.Series(np.cumsum(np.random.randn(60)), 
                             index=dxy.index, name="China Credit Impulse (Simulated)")
    btc = pd.Series(np.cumsum(np.random.randn(60)*1000) + 30000, 
                    index=dxy.index, name="BTC/USD (Simulated)")

    # --- Alerts ---
    if gas.iloc[-1] < 3:
        st.warning("⛽️ Gasoline below $3 — consumer pressure point.")

    if gold.iloc[-1] > 2100:
        st.info("🥇 Gold > $2100 — flight to safety underway.")

    # --- Charts ---
    st.subheader("💵 DXY (Dollar Index)")
    plot_time_series(dxy, "US Dollar Index (DXY)", alert_level=105)

    st.subheader("🌍 EM FX Index (Simulated)")
    plot_time_series(em_fx, em_fx.name)

    st.subheader("🇨🇳 China Credit Impulse (Simulated)")
    plot_time_series(china_credit, china_credit.name)

    st.subheader("🛢️ WTI Crude & ⛽ Gasoline Prices")
    plot_time_series(pd.concat([wti, gas], axis=1), "Oil vs Gasoline", alert_level=None)

    st.subheader("🪙 Gold & Bitcoin (Simulated BTC)")
    plot_time_series(pd.concat([gold, btc], axis=1), "Gold & BTC", alert_level=None)
