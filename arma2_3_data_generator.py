import pandas as pd
import numpy as np
from statsmodels.tsa.arima_process import ArmaProcess

# Set random seed for reproducibility
np.random.seed(0)

# Define ARMA(2,3) parameters
ar_coefs = [0.5, -0.3]  # Autoregressive coefficients
ma_coefs = [0.2, 0.1, -0.1]  # Moving average coefficients

# Create ARMA(2,3) process
arma_process = ArmaProcess(ar_coefs, ma_coefs)

# Generate ARMA(2,3) data
num_points = 100
data = arma_process.generate_sample(nsample=num_points)

# Create DateTimeIndex
index = pd.date_range(start='2022-01-01', periods=num_points, freq='D')

# Create DataFrame with labeled date column
df = pd.DataFrame({'Date': index, 'Value': data})

# Save to CSV file
df.to_csv('arma2_3_time_series_data.csv', index=False)  # Setting index=False to exclude