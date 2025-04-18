import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objs as go
from sentiment.twitter_sentiment import get_sentiment_dataframe
from data.price_data import get_intraday_prices

# --- Main layout ---
def show_trading_terminal():
    st.set_page_config(page_title="Trading Terminal", layout="wide")

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

    # --- Ticker Selection ---
    st.markdown('<div class="section-header">Market Price</div>', unsafe_allow_html=True)
    symbol = st.selectbox("Select Ticker", ["SPY", "GOOG", "AAPL", "TSLA"])
    col_left, col_right = st.columns([3, 1])

    # --- Live Chart ---
    with col_left:
        try:
            df = get_intraday_prices(symbol)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df["datetime"], y=df["price"], mode="lines", name=symbol))
            fig.update_layout(
                height=300,
                margin=dict(l=20, r=20, t=10, b=10),
                xaxis_title="Time",
                yaxis_title="Price",
                template="plotly_dark"
            )
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Live price error: {e}")

    # --- Price Metrics ---
    with col_right:
        st.metric("Price", "2,251.41", "+3.39")
        st.metric("Volume", "0.49M")
        st.metric("Change", "0.15%")
        st.metric("52W High", "3,042.00")
        st.metric("52W Low", "2,202.27")

    # --- Twitter Sentiment ---
    st.markdown('<div class="section-header">🐦 Twitter Sentiment</div>', unsafe_allow_html=True)
    try:
        sentiment_df = get_sentiment_dataframe(symbol)
        avg_sentiment = sentiment_df["score"].mean()
        st.metric("Average Sentiment", f"{avg_sentiment:+.2f}")
        st.line_chart(sentiment_df.set_index("timestamp")["score"])
        st.markdown("### Recent Tweets")
        for _, row in sentiment_df.head(5).iterrows():
            emoji = "🟢" if row["score"] > 0.2 else "🔴" if row["score"] < -0.2 else "⚪"
            st.write(f"{emoji} {row['text']}")
    except Exception as e:
        st.error(f"Sentiment error: {e}")

    # --- Confidence Gauge ---
    st.markdown('<div class="section-header">Buy Confidence</div>', unsafe_allow_html=True)
    st.progress(0.7)

    # --- Fake Live Tweets Feed ---
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
