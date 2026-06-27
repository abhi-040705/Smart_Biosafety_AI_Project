# 🧪 AI-Based Smart Biosafety Monitoring and RFID Access Control System

An IoT and AI-powered laboratory safety monitoring system developed using **ESP32**, **RFID**, **DHT11**, **MQ135**, **Flask**, **Streamlit**, and **Machine Learning**.

The system continuously monitors environmental conditions, provides secure RFID-based access control, predicts future sensor values using AI, detects anomalies, and visualizes all data through a real-time dashboard.

---

## 📌 Project Overview

Maintaining a safe laboratory environment requires continuous monitoring of environmental parameters and secure access control. Traditional monitoring systems rely on manual supervision and do not provide predictive analytics or centralized visualization.

This project solves these challenges by integrating IoT hardware with Artificial Intelligence.

### The system can:

* 🌡 Monitor Temperature
* 💧 Monitor Humidity
* ☣ Monitor Air Quality using MQ135
* 🔐 Authenticate users using RFID
* 🚪 Automatically open and close the laboratory door using a Servo Motor
* 🔔 Trigger a buzzer during unauthorized access
* 📡 Send sensor data over WiFi
* 📊 Display live data on a Streamlit dashboard
* 🤖 Predict future sensor values using Machine Learning
* ⚠ Detect abnormal environmental conditions

---

# ✨ Features

* Real-time Temperature Monitoring
* Real-time Humidity Monitoring
* Gas Leakage Detection
* RFID Based Access Control
* Automatic Door Lock System
* Buzzer Alert for Unauthorized Access
* Flask Backend Server
* CSV Data Logging
* AI Prediction using Linear Regression
* Anomaly Detection using Isolation Forest
* Interactive Streamlit Dashboard
* Live Graphs and Gauges

---

# 🛠 Hardware Components

| Component                 | Purpose                |
| ------------------------- | ---------------------- |
| ESP32 Development Board   | Main Controller        |
| DHT11 Sensor              | Temperature & Humidity |
| MQ135 Sensor              | Air Quality Monitoring |
| RC522 RFID Module         | User Authentication    |
| RFID Card/Tag             | Secure Access          |
| SG90 Servo Motor          | Door Lock Mechanism    |
| Buzzer                    | Alarm System           |
| Breadboard & Jumper Wires | Connections            |

---

# 💻 Software Stack

* Arduino IDE
* Python 3
* Flask
* Streamlit
* Plotly
* Pandas
* Scikit-Learn
* Joblib
* VS Code

---

# 📂 Project Structure

```
Smart_Biosafety_AI_Project
│
├── backend
│   ├── server.py
│   ├── train_model.py
│   ├── sensor_data.csv
│   ├── access_logs.csv
│   ├── temp.pkl
│   ├── hum.pkl
│   ├── gas.pkl
│   └── utils.py
│
├── dashboard
│   └── app.py
│
├── esp32_biosafety.ino
│
├── README.md
└── .gitignore
```

---

# 🔌 ESP32 Pin Connections

| Component    | ESP32 Pin |
| ------------ | --------- |
| DHT11 Data   | GPIO 4    |
| MQ135 Analog | GPIO 34   |
| Servo Signal | GPIO 13   |
| Buzzer       | GPIO 27   |
| RFID SDA     | GPIO 5    |
| RFID SCK     | GPIO 18   |
| RFID MOSI    | GPIO 23   |
| RFID MISO    | GPIO 19   |
| RFID RST     | GPIO 22   |

---

# ⚙ Working Principle

1. ESP32 reads temperature, humidity and gas values.
2. Sensor data is transmitted to the Flask server over WiFi.
3. Flask stores sensor values in `sensor_data.csv`.
4. RFID cards are authenticated.
5. Authorized users open the servo-controlled door.
6. Unauthorized users trigger the buzzer.
7. Access logs are stored in `access_logs.csv`.
8. Machine Learning predicts future sensor values.
9. Isolation Forest detects anomalies.
10. Streamlit displays live sensor values, graphs, AI predictions and access logs.

---

# 🤖 Artificial Intelligence

## Linear Regression

Three machine learning models are trained:

* Temperature Prediction
* Humidity Prediction
* Gas Value Prediction

These models estimate future environmental conditions using historical sensor data.

---

## Isolation Forest

Isolation Forest continuously checks sensor values for abnormal behaviour.

Examples of anomalies:

* Sudden increase in gas concentration
* High temperature
* Abnormal humidity

When detected, the dashboard displays an anomaly warning.

---

# 📊 Streamlit Dashboard

The dashboard displays:

* 🌡 Live Temperature
* 💧 Live Humidity
* ☣ Live Gas Value
* 📈 Sensor Trends
* 🎯 Gauge Meters
* 🤖 AI Predictions
* ⚠ Safety Status
* 🔐 RFID Access Logs
* 📥 Download Sensor Data

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/abhi-040705/Smart_Biosafety_AI_Project.git
```

---

## Install Python Dependencies

```bash
pip install flask
pip install pandas
pip install streamlit
pip install plotly
pip install scikit-learn
pip install joblib
```

---

## Start Flask Server

```bash
cd backend
python3 server.py
```

---

## Train Machine Learning Models

```bash
cd backend
python3 train_model.py
```

---

## Run Dashboard

```bash
cd dashboard
streamlit run app.py
```

---

# 📈 Future Scope

* Firebase Cloud Integration
* Mobile Application
* Camera-Based PPE Detection
* Face Recognition
* SMS and Email Alerts
* Cloud Database
* Real-Time Notifications
* Multi-Laboratory Monitoring

---

# 🎯 Applications

* Research Laboratories
* Biosafety Laboratories
* Hospitals
* Pharmaceutical Industries
* Educational Institutions
* Chemical Industries
* Smart Buildings

---

# 👨‍💻 Author

**Abhishek Gaurav**

Electronics and Telecommunication Engineering

RV College of Engineering

---

# 📜 License

This project is intended for educational and academic purposes.
