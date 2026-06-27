import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
from sklearn.ensemble import IsolationForest

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Biosafety Dashboard",
    layout="wide"
)

st_autorefresh(interval=2000)

st.title("🧪 AI Smart Biosafety Monitoring System")

# ---------------- LOAD DATA ----------------

sensor_df = pd.read_csv(
    "../backend/sensor_data.csv",
    engine="python"
)

access_df = pd.read_csv(
    "../backend/access_logs.csv",
    engine="python"
)

# ---------------- CURRENT VALUES ----------------

current_temp = float(sensor_df.iloc[-1]["temperature"])
current_hum = float(sensor_df.iloc[-1]["humidity"])
current_gas = float(sensor_df.iloc[-1]["gas"])

# ---------------- METRICS ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🌡 Temperature (°C)",
        round(current_temp, 2)
    )

with c2:
    st.metric(
        "💧 Humidity (%)",
        round(current_hum, 2)
    )

with c3:
    st.metric(
        "☣ Gas Value",
        int(current_gas)
    )

# ---------------- SAFETY STATUS ----------------

st.subheader("Safety Status")

if current_gas < 300:
    st.success("🟢 SAFE")

elif current_gas < 450:
    st.warning("🟡 MODERATE RISK")

else:
    st.error("🔴 HIGH RISK")

# ---------------- GAUGES ----------------

g1, g2, g3 = st.columns(3)

with g1:
    fig_temp = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_temp,
        title={'text': "Temperature"}
    ))
    st.plotly_chart(fig_temp, use_container_width=True)

with g2:
    fig_hum = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_hum,
        title={'text': "Humidity"}
    ))
    st.plotly_chart(fig_hum, use_container_width=True)

with g3:
    fig_gas = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_gas,
        title={'text': "Gas Value"}
    ))
    st.plotly_chart(fig_gas, use_container_width=True)

# ---------------- SENSOR GRAPHS ----------------

st.subheader("Sensor Trends")

fig1 = px.line(
    sensor_df,
    x="time",
    y="temperature",
    title="Temperature vs Time"
)

fig2 = px.line(
    sensor_df,
    x="time",
    y="humidity",
    title="Humidity vs Time"
)

fig3 = px.line(
    sensor_df,
    x="time",
    y="gas",
    title="Gas vs Time"
)

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)

# ---------------- ANOMALY DETECTION ----------------

st.subheader("AI Anomaly Detection")

iso = IsolationForest(contamination=0.05)

sensor_df["anomaly"] = iso.fit_predict(
    sensor_df[["temperature", "humidity", "gas"]]
)

if sensor_df["anomaly"].iloc[-1] == -1:
    st.error("⚠️ ANOMALY DETECTED")
else:
    st.success("NORMAL")

# ---------------- LAST RFID ACCESS ----------------

st.subheader("Last RFID Access")

latest = access_df.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"UID\n\n{latest['uid']}")

with col2:
    st.success(f"Status\n\n{latest['status']}")

with col3:
    st.warning(f"Door\n\n{latest['door']}")

# ---------------- ACCESS LOGS ----------------

st.subheader("Recent Access Logs")

st.dataframe(
    access_df.tail(10),
    use_container_width=True
)

# ---------------- DOWNLOAD BUTTON ----------------

st.download_button(
    "Download Sensor Data",
    sensor_df.to_csv(index=False),
    file_name="sensor_data.csv"
)

# ---------------- DEBUG SECTION ----------------

st.subheader("Latest Sensor Row")

st.write(sensor_df.tail(1))