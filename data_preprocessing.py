import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('sensor_data.csv')

# Data Preprocessing
features = data[['temperature', 'vibration', 'pressure']]
labels = data['maintenance_required']

# Standardizing the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print("Data Preprocessed Successfully")
