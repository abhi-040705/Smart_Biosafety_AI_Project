from flask import Flask, request
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# ---------- Sensor Data ----------
@app.route('/data', methods=['POST'])
def receive_sensor_data():

    data = request.json

    sensor_row = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "gas": data["gas"]
    }

    df = pd.DataFrame([sensor_row])

    if os.path.exists("sensor_data.csv"):
        df.to_csv(
            "sensor_data.csv",
            mode='a',
            header=False,
            index=False
        )
    else:
        df.to_csv(
            "sensor_data.csv",
            index=False
        )

    return {"status": "sensor data received"}


# ---------- RFID Access Logs ----------
@app.route('/access', methods=['POST'])
def receive_access_log():

    data = request.json

    access_row = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "uid": data["uid"],
        "status": data["status"],
        "door": data["door"]
    }

    df = pd.DataFrame([access_row])

    if os.path.exists("access_logs.csv"):
        df.to_csv(
            "access_logs.csv",
            mode='a',
            header=False,
            index=False
        )
    else:
        df.to_csv(
            "access_logs.csv",
            index=False
        )

    return {"status": "access log received"}


# ---------- Main ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)