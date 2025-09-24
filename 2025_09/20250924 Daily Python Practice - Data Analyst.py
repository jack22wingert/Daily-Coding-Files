# 20250924 Daily Python Practice - Data Analyst
# Task: Analyze time series data: aggregate by month, calculate trends, and visualize

import pandas as pd 
import matplotlib.pyplot as plt

#sample sales dataset over several months
data = {
      "Date": pd.date_range(start="2025-01-01", periods=12, freq="M"),
    "Region": ["North", "South", "East", "West"] * 3,
    "Sales": [2300, 1700, 2500, 2100, 2400, 1800, 2600, 2200, 2500, 1900, 2700, 2300]  
}

df = pd.DataFrame(data)

# Convert 'Date' to datetime 
df["Date"] = pd.to_datetime(df["Date"])

# Extract month for aggregation
df["Month"] = df["Date"].dt.strftime("%Y-%m")

# Aggregate total sales by month
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

# Calculate rolling 3-month average
monthly_sales["RollingAvg"] = monthly_sales["Sales"].rolling(window=3).mean()

print("Monthly Sales and 3-Month Rolling Average:")
print(monthly_sales)

# Visualization
plt.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", label="Monthly Sales")
plt.plot(monthly_sales["Month"], monthly_sales["RollingAvg"], marker="x", linestyle="--", label="3-Month Rolling Avg")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend with Rolling Average")
plt.legend()
plt.tight_layout()
plt.show()




