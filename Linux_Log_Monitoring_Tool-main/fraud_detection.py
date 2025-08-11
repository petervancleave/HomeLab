import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("ssh_logs.csv")

# convert categorical data to numerical data
df["Status"] = df["Status"].map({"Accepted": 1, "Failed": 0})

# IP addresses for anomaly detection 
df["IP_numeric"] = df["IP"].astype("category").cat.codes

# Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
df["Anomaly"] = model.fit_predict(df[["Status", "IP_numeric"]])

# Print flags
anomalies = df[df["Anomaly"] == -1]
print("🚨 Potential Fraudulent Activities Detected:")
print(anomalies)
