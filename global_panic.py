import streamlit as st
from data.fetch_fred import (
    get_dxy, get_wti, get_gasoline, get_gold,
    get_em_fx, get_china_industrial_prod
)
from data.fetch_alt import get_btc_usd
from dashboard.plots import plot_time_series
from datetime import datetime

def global_panic_tab():
    st.markdown("## 🌎 Global Panic Indicators")

    with st.spinner("Loading real-time data..."):
        dxy = get_dxy().last('60D')
        em_fx = get_em_fx().last('60D')
        china = get_china_industrial_prod().last('60D')
        wti = get_wti().last('60D')
        gas = get_gasoline().last('60D')
        gold = get_gold().last('60D')
        btc = get_btc_usd().last('60D')
        last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    st.caption(f"🔄 Data last updated: {last_updated}")

    # Alerts
    st.markdown("### 🚨 Alerts")
    if gas.iloc[-1] < 3:
        st.warning("⛽ Gasoline < $3 — consumer pressure alert.")
    if gold.iloc[-1] > 2100:
        st.info("🥇 Gold > $2100 — flight to safety activated.")
    if dxy.iloc[-1] > 105:
        st.warning("💵 DXY above 105 — dollar strength squeeze risk.")

    # Charts
    st.markdown("---")
    with st.expander("💵 DXY (US Dollar Index)"):
        plot_time_series(dxy, dxy.name, alert_level=105)

    with st.expander("🌍 USD vs EM FX"):
        plot_time_series(em_fx, em_fx.name)

    with st.expander("🇨🇳 China Industrial Production"):
        plot_time_series(china, china.name)

    with st.expander("🛢️ WTI vs Gasoline"):
        plot_time_series(wti.to_frame().join(gas), "WTI vs Gasoline")

    with st.expander("🥇 Gold & ₿ Bitcoin"):
        plot_time_series(gold.to_frame().join(btc), "Gold & BTC")
