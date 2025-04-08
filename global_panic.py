import streamlit as st
from data.fetch_fred import get_dxy, get_wti, get_gasoline, get_gold, get_em_fx, get_china_loans_yoy
from dashboard.plots import plot_time_series
from data.fetch_alt import get_btc_usd  # You may need to create this if it’s in a separate file

def global_panic_tab():
    st.header("🌎 Global Panic Indicators")

    # Fetch all real data
    with st.spinner("Loading real data..."):
        dxy = get_dxy().last('60D')
        em_fx = get_em_fx().last('60D')
        china_credit = get_china_loans_yoy().last('60D')
        wti = get_wti().last('60D')
        gas = get_gasoline().last('60D')
        gold = get_gold().last('60D')
        btc = get_btc_usd().last('60D')

    # Alerts
    if gas.iloc[-1] < 3:
        st.warning("⛽ Gasoline < $3 — consumer pressure alert.")
    if gold.iloc[-1] > 2100:
        st.info("🥇 Gold > $2100 — flight to safety activated.")
    if dxy.iloc[-1] > 105:
        st.warning("💵 DXY above 105 — dollar strength squeeze risk.")

    # Charts
    st.subheader("💵 DXY (US Dollar Index)")
    plot_time_series(dxy, dxy.name, alert_level=105)

    st.subheader("🌍 USD vs EM FX (Trade-Weighted)")
    plot_time_series(em_fx, em_fx.name)

    st.subheader("🇨🇳 China Loan Growth (YoY)")
    plot_time_series(china_credit, china_credit.name)

    st.subheader("🛢️ WTI Crude & ⛽ Gasoline")
    plot_time_series(wti.to_frame().join(gas), "WTI vs Gasoline")

    st.subheader("🥇 Gold & ₿ Bitcoin")
    plot_time_series(gold.to_frame().join(btc), "Gold & BTC")
