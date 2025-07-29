# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

# Load data
df = pd.read_csv("motor_data.csv")

X = df[['ambient', 'coolant', 'u_d', 'u_q', 'i_d', 'i_q', 'motor_speed', 'torque', 'stator_yoke', 'stator_tooth', 'stator_winding']]
y = df['pm']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestRegressor()
model.fit(X_scaled, y)

# Save the model and scaler
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
