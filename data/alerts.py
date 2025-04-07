def check_alerts(vix, spread, dxy):
    alerts = []

    if vix.iloc[-1] > 25:
        alerts.append(f"VIX above 25! Current: {vix.iloc[-1]:.2f}")

    if spread.iloc[-1] < 0:
        alerts.append(f"Yield curve inverted! 10Y-2Y spread: {spread.iloc[-1]:.2f} bps")

    if dxy.iloc[-1] > 105:
        alerts.append(f"DXY strong above 105. Current: {dxy.iloc[-1]:.2f}")

    return alerts
