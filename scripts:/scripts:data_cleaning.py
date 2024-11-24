import pandas as pd

# Load the data
data = pd.read_csv("/Users/sanjojoy/Desktop/Git_repositories/Sales forecasting/data/sales_data.csv")

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Aggregate sales data by day
sales = data.groupby('date').sum()

# Reset the index so 'date' becomes a column again
sales.reset_index(inplace=True)

output_path = "/Users/sanjojoy/Desktop/GIt_repositories/Sales forecasting/data/cleaned_sales_data2.csv"

# Save the file to the absolute path
sales.to_csv(output_path, index=False)

print(f"File saved to {output_path}")