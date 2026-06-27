import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load sensor data
df = pd.read_csv("sensor_data.csv")

# X-axis = sample number
X = df.index.values.reshape(-1, 1)

# ---------------- Temperature Model ----------------
temp_model = LinearRegression()
temp_model.fit(X, df["temperature"])

# ---------------- Humidity Model ----------------
hum_model = LinearRegression()
hum_model.fit(X, df["humidity"])

# ---------------- Gas Model ----------------
gas_model = LinearRegression()
gas_model.fit(X, df["gas"])

# Save models
joblib.dump(temp_model, "temp.pkl")
joblib.dump(hum_model, "hum.pkl")
joblib.dump(gas_model, "gas.pkl")

print("Models trained successfully!")