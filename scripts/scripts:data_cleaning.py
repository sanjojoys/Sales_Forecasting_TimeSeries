import pandas as pd

# Load the data
data = pd.read_csv("/Users/sanjojoy/Desktop/GIt_repositories/Sales forecasting/data/sales_data.csv")

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Aggregate sales data by day
sales = data.groupby('date').sum()

# Save the processed data
sales.to_csv("data/cleaned_sales_data.csv")