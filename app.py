import streamlit as st

st.set_page_config(
    page_title="Test App",
    layout="wide"
)

st.title("Testing Trading Terminal")

try:
    from dashboard.trading_terminal import show_trading_terminal
    st.success("✅ Imported successfully")

    st.markdown("---")
    show_trading_terminal()
except Exception as e:
    st.error(f"❌ Exception: {e}")
