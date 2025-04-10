import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objs as go

# Placeholder price data
def mock_intraday_data():
    now = datetime.utcnow()
    times = [now - timedelta(minutes=5 * i) for i in range(60)][::-1]
    prices = np.cumsum(np.random.randn(60)) + 2250
    return pd.DataFrame({"time": times, "price": prices})

# Main layout
def show_trading_terminal():
    st.markdown(
        """
        <style>
            .section-header {
                font-size: 1.2rem;
                font-weight: 600;
                margin-bottom: 10px;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Top Cards ---
    st.markdown("## 📝 Market Overview")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("S&P 500", "4,216.33", "-0.45%")
    col2.metric("NASDAQ", "13,410.22", "+0.63%")
    col3.metric("DOW", "34,234.11", "-0.31%")
    col4.metric("VIX", "19.12", "+0.87%")

    # --- Global Market Chart ---
    st.markdown("### 📈 Global Market State")
    dummy = pd.DataFrame({
        "S&P 500": np.cumsum(np.random.randn(100)) + 3900,
        "NASDAQ": np.cumsum(np.random.randn(100)) + 11500,
        "DOW": np.cumsum(np.random.randn(100)) + 31000,
        "VIX": np.cumsum(np.random.randn(100)) + 30,
    })

    st.line_chart(dummy)

    # --- Market Price Chart + Right Panel ---
    st.markdown('<div class="section-header">Market Price</div>', unsafe_allow_html=True)
    col_left, col_right = st.columns([3, 1])

    with col_left:
        df = mock_intraday_data()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["time"], y=df["price"], mode="lines", name="GOOG"))
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=10, b=10),
            xaxis_title="Time",
            yaxis_title="Price",
            template="plotly_dark"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.metric("Price", "2,251.41", "+3.39")
        st.metric("Volume", "0.49M")
        st.metric("Change", "0.15%")
        st.metric("52W High", "3,042.00")
        st.metric("52W Low", "2,202.27")

    # --- Twitter Sentiment ---
    st.markdown('<div class="section-header">Twitter Sentiment Analysis</div>', unsafe_allow_html=True)
    times = pd.date_range(end=datetime.utcnow(), periods=60)
    sentiment = np.random.normal(0, 0.5, 60).cumsum()
    st.line_chart(pd.DataFrame({"Sentiment": sentiment}, index=times))

    # --- Buy Confidence Gauge Placeholder ---
    st.markdown('<div class="section-header">Buy Confidence</div>', unsafe_allow_html=True)
    st.progress(0.7)

    # --- Live Tweets ---
    st.markdown('<div class="section-header">📰 Twitter Feed</div>', unsafe_allow_html=True)
    st.info("🔄 Soon: Real tweet feed from financial accounts or sentiment scraping.")
    st.write("""
    - `[13:07 UTC]` CNBC: Elon Musk said he’s voting Republican...
    - `[13:05 UTC]` Benzinga: LIVE Options Game with @TradePro
    - `[13:03 UTC]` Reuters: Oil prices spike on Iran tensions...
    - `[13:01 UTC]` Bloomberg: Dollar retreats amid treasury volatility
    """)

    st.markdown("---")
    st.caption("Prototype trading terminal built by Ned. Real-time integrations coming next.")
