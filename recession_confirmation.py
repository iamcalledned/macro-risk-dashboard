import streamlit as st
from data.fetch_fred import (
    get_consumer_credit,
    get_nonrevolving_credit,
    get_auto_loan_rate
)
from dashboard.plots import plot_time_series

def recession_confirmation_tab():
    st.header("📉 Recession Confirmation")

    # Get Data
    credit_total = get_consumer_credit().last('60D')
    non_revolving = get_nonrevolving_credit().last('60D')
    auto_rate = get_auto_loan_rate().last('60D')

    # Show current values
    col1, col2, col3 = st.columns(3)
    col1.metric("Consumer Credit Total", f"${credit_total.iloc[-1]:,.0f}B")
    col2.metric("Non-Revolving Credit", f"${non_revolving.iloc[-1]:,.0f}B")
    col3.metric("Auto Loan Rate", f"{auto_rate.iloc[-1]:.2f}%")

    # Alert logic
    if auto_rate.iloc[-1] > 8.0:
        st.error("🚗 Auto loan rate above 8% — consumer stress is high.")

    if credit_total.iloc[-1] < credit_total.iloc[-2]:
        st.warning("📉 Total consumer credit declined — possible early signal of credit tightening.")

    # Charts
    st.subheader("🧾 Consumer Credit Outstanding")
    plot_time_series(credit_total, "Consumer Credit Total")

    st.subheader("📄 Non-Revolving Credit")
    plot_time_series(non_revolving, "Non-Revolving Credit")

    st.subheader("🚙 Auto Loan 60-Month Rate")
    plot_time_series(auto_rate, "Auto Loan Rate", alert_level=8.0)
