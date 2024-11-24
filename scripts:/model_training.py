import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the cleaned sales data
file_path = "/Users/sanjojoy/Desktop/Git_repositories/Sales forecasting/data/cleaned_sales_data.csv"
sales = pd.read_csv(file_path)

# Ensure 'date' is a datetime and set it as the index
if 'date' in sales.columns:
    sales['date'] = pd.to_datetime(sales['date'])
    sales.set_index('date', inplace=True)

# Define and fit the ARIMA model
model = ARIMA(sales['sales'], order=(5, 1, 0))  # (p, d, q)
model_fit = model.fit()

# Summarize the model
print(model_fit.summary())

# Forecasting: Predict the next 10 values
forecast = model_fit.forecast(steps=10)  # Forecast 10 steps ahead
print("Forecasted values:", forecast)

# Assuming you have actual values for comparison
# Replace the following line with your actual observed values
actual = sales['sales'][-10:]  # Example: last 10 actual values

# Calculate Mean Squared Error
mse = mean_squared_error(actual, forecast[:len(actual)])
print(f"Mean Squared Error: {mse}")

# Optionally calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")