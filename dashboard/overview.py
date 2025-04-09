import streamlit as st
from datetime import datetime
from streamlit.components.v1 import html

from data.fetch_fred import (
    get_vix,
    get_dxy,
    get_fed_funds,
    get_baml_hy,
    get_baml_ig
)

from data.fetch_alt import get_sp500  # New function you'll want in fetch_alt.py


def show_main_dashboard():
    # Header
    st.markdown(f"""
        <style>
            .main-header {{
                background-color: #0e1117;
                color: white;
                padding: 1rem 2rem;
                font-size: 1.8rem;
                font-weight: 700;
                border-bottom: 2px solid #1f232e;
            }}
            .sub-header {{
                font-size: 1rem;
                color: #999;
                margin-top: -1rem;
                margin-bottom: 1.5rem;
            }}
        </style>
        <div class="main-header">📈 Global Market Stress Monitor</div>
        <div class="sub-header">A real-time dashboard for macro chaos. Updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}</div>
    """, unsafe_allow_html=True)
    # --- Pull Live Data ---
    try:
        vix = get_vix().last('2D')
        dxy = get_dxy().last('2D')
        fed_funds = get_fed_funds().last('2D')
        hy = get_baml_hy().last('2D')
        ig = get_baml_ig().last('2D')
        spx = get_sp500()
        hy_ig_spread = hy.iloc[-1] - ig.iloc[-1]
        hy_ig_delta = (hy - ig).iloc[-1] - (hy - ig).iloc[-2]
    except Exception as e:
        st.error(f"⚠️ Error fetching data: {e}")
        return

    # Metrics Row
    with st.container():
        st.markdown("### 🔍 Key Market Metrics")
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("VIX", f"{vix.iloc[-1]:.2f}", f"{vix.iloc[-1] - vix.iloc[-2]:+.2f}")
        col2.metric("S&P 500", f"{spx.iloc[-1]:,.0f}", f"{spx.iloc[-1] - spx.iloc[-2]:+.0f}")
        col3.metric("DXY", f"{dxy.iloc[-1]:.2f}", f"{dxy.iloc[-1] - dxy.iloc[-2]:+.2f}")
        col4.metric("HY–IG", f"{hy_ig_spread:.1f} bps", f"{hy_ig_delta:.1f}")
        col5.metric("Fed Funds", f"{fed_funds.iloc[-1]:.2f}%", f"{fed_funds.iloc[-1] - fed_funds.iloc[-2]:+.2f}%")

    st.markdown("---")

    # Dashboard Grid
    col_left, col_right = st.columns([2, 1])

    with col_left:
        with st.container():
            st.markdown("### 🧠 Market Stress")
            st.line_chart(data=None, height=200)

        with st.container():
            st.markdown("### 💳 Credit & Liquidity")
            st.line_chart(data=None, height=200)

        with st.container():
            st.markdown("### 🧮 Macro & Fed Watch")
            st.line_chart(data=None, height=200)

        with st.container():
            st.markdown("### 📉 Recession Confirmation")
            st.line_chart(data=None, height=200)

    with col_right:
        st.markdown("### 📰 Live Market Headlines")
        st.info("🔄 Coming soon: Embedded Twitter, RSS, or scraped headlines.")
        html("""
            <div style='height: 450px; overflow-y: scroll; background: #f9f9f9; padding: 1rem; border: 1px solid #ddd;'>
                <p><b>[ZeroHedge]</b> S&P futures surge after Fed minutes...</p>
                <p><b>[Bloomberg]</b> Dollar retreats amid treasury volatility...</p>
                <p><b>[Reuters]</b> Oil prices spike as Iran tensions rise...</p>
                <p><b>[CNBC]</b> Jobless claims come in lower than expected...</p>
                <p><i>Live RSS or X feed will go here.</i></p>
            </div>
        """, height=500)

    # Footer
    st.markdown("---")
    st.caption("Built by Ned | Powered by Streamlit & real-time market APIs")
