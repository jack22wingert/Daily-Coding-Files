# 20250920 Daily Python Practice - Data Analyst
# Task: Load a dataset, perform exploratory data analysis (EDA), and visualize key insights

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample sales dataset
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Sales": [2300, 1700, 2500, 2100, 1900, 1600, 2200, 2000],
    "Profit": [400, 300, 500, 350, 320, 280, 450, 330]
}

df = pd.DataFrame(data)

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Group by region
region_summary = df.groupby("Region").agg({"Sales":"mean","Profit":"mean"}).reset_index()
print("\nAverage Sales & Profit by Region:")
print(region_summary)

# Visualization: Sales by Region
plt.bar(region_summary["Region"], region_summary["Sales"])
plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
