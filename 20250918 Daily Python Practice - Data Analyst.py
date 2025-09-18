# 20250918 Daily Python Practice - Data Analyst
# Task: Create a small dataset, calculate summary statistics, and sort results. 

import pandas as pd 

# Create a simple DataFrame (liek mock sales data)
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Units_Sold": [15, 120, 75, 30, 60], 
    "Price": [1200, 25, 45, 200, 80]
}

df = pd.DataFrame(data)

#Calculate total revenue per product
df["Revenue"] = df["Units_Sold"] * df["Price"]

#Sort products by revenue
df_sorted = df.sort_values(by="Revenue", ascending=False)

# Show Summary statistics
summary = df.describe()

print(" Daily Python Practice (20025-09-18)")
print("\n-- Sales Data ---")
print(df)
print("\n-- Sorted by Revenue ---")
print(df_sorted)
print("\n-- Summary Statistics ---")
print(summary)