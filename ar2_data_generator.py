import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Parameters for AR(2) process
phi1 = 0.6
phi2 = -0.3
num_points = 100

# Generate white noise
white_noise = np.random.normal(0, 1, num_points)

# Initialize array to store data
data = np.zeros(num_points)

# Generate AR(2) process data
data[0] = white_noise[0]
data[1] = phi1 * white_noise[0] + phi2 * white_noise[1] + white_noise[1]
for t in range(2, num_points):
    data[t] = phi1 * data[t-1] + phi2 * data[t-2] + white_noise[t]

# Create DateTimeIndex
index = pd.date_range(start='2022-01-01', periods=num_points, freq='D')

# Create DataFrame with labeled date column
df = pd.DataFrame({'Date': index, 'Value': data})

# Save to CSV file
df.to_csv('ar2_time_series_data.csv', index=False)  # Setting index=False to exclude