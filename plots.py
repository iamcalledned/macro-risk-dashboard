import streamlit as st
import matplotlib.pyplot as plt

def plot_time_series(data, title, alert_level=None):
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set_title(title)
    if alert_level is not None:
        ax.axhline(alert_level, color='red', linestyle='--', label='Alert Threshold')
        ax.legend()
    st.pyplot(fig)
