import streamlit as st
from dashboard.layout import show_line_chart

def global_panic_tab():
    st.header("🌎 Global Panic Indicators")

    # DXY Index
    show_line_chart(
        title="DXY Index",
        data_source="USD_INDEX",
        alerts=[]
    )

    # EM FX Index
    show_line_chart(
        title="EM FX Index",
        data_source="EM_FX",
        alerts=[]
    )

    # China Credit Impulse
    show_line_chart(
        title="China Credit Impulse",
        data_source="CHINA_CREDIT",
        alerts=[]
    )

    # WTI Crude & Gasoline Prices
    show_line_chart(
        title="WTI Crude & Gasoline Prices",
        data_source=["WTI", "GASOLINE"],
        alerts=["gas_below_3"]
    )

    # Gold & Bitcoin
    show_line_chart(
        title="Gold & Bitcoin",
        data_source=["GOLD_SPOT", "BTC_USD"],
        alerts=[]
    )
