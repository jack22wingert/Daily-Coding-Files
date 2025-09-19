# 20250919 Daily Python Practice - Data Analyst
# Task: Simulate a CSV dataset, clean data, and generate summary statistics

import pandas as pd
import numpy as np

#Simulate CSV data (like sales with missing values)
data = {
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006], 
    "Customer": ["Alice", "Bob", "Charlie", "David", np.nan, "Frank"], 
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse"],
    "Quantity": [1,2,1,np.nan, 3, 2],
    "Price": [1200, 25, 45, 200, 1200, 25]
}

df = pd.DataFrame(data)

# Show original data
print("Original Data")
print(df)

# Fill Missing values
df['Customer'] = df['Customer'].fillna("Unknown")
df['Quantity'] = df['Quantity'].fillna(1)

# Revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# Group by Product and summarize revenue
product_summary = df.groupby('Product')['Revenue'].sum().reset_index()

#Display summary
print("/n--- Cleaned Data ---")
print(df)
print("/n--- Product Revenue Summary ---")
print(product_summary)


