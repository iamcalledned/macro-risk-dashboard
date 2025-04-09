import streamlit as st
from data.fetch_fred import get_fed_funds, get_5y5y_breakeven, get_cpi_yoy, get_10y2y_spread
from dashboard.plots import plot_time_series
from datetime import datetime

def macro_fed_watch_tab():
    st.markdown("## 🧮 Macro & Fed Watch")

    with st.spinner("Loading real-time data..."):
        fed_funds = get_fed_funds().last('60D')
        breakeven = get_5y5y_breakeven().last('60D')
        cpi = get_cpi_yoy().last('60D')
        spread = get_10y2y_spread().last('60D')
        last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    st.caption(f"🔄 Data last updated: {last_updated}")

    # Metrics
    st.markdown("### 📊 Macro Snapshot")
    col1, col2, col3 = st.columns(3)
    col1.metric("Fed Funds Rate", f"{fed_funds.iloc[-1]:.2f}%")
    col2.metric("5Y5Y Inflation", f"{breakeven.iloc[-1]:.2f}%")
    col3.metric("CPI YoY", f"{cpi.iloc[-1]:.2f}%")

    # Charts
    st.markdown("---")
    with st.expander("🏦 Fed Funds Rate"):
        plot_time_series(fed_funds, "Fed Funds Rate")

    with st.expander("📉 Yield Curve (10Y - 2Y)"):
        plot_time_series(spread * 100, "10Y–2Y Spread (bps)", alert_level=0)

    with st.expander("📊 5Y5Y Inflation Breakeven"):
        plot_time_series(breakeven, "5Y5Y Inflation Breakeven")

    with st.expander("📈 CPI Year-over-Year"):
        plot_time_series(cpi, "Consumer Price Index YoY")
