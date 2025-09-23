# 20250922 Daily Python Practice - Data Analyst
# Task: Merge multiple datasets, identify missing values, and generate joined summaries

import pandas as pd

# Employee information dataset
employees = {
    "EmployeeID": [101, 102, 103, 104, 105], 
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Department": ["Sales", "Sales", "HR", "IT", "IT"]
}

# Salary dataset
salaries = {
    "EmployeeID": [101, 102, 104, 105, 106], # 106 is not in employees dataset
    "Salary": [55000, 60000, 52000, 70000, 58000]
}

#Bonus dataset
bonuses = {
    "EmployeeID": [101, 103, 104, 105], 
    "Bonus": [5000, 3000, 3200, 8500]
}

# Convert to DataFrames
df_employees = pd.DataFrame(employees)
df_salaries = pd.DataFrame(salaries)
df_bonuses = pd.DataFrame(bonuses)

# Merge employees with salaries (Left join keeps all employees)
df_merge1 = pd.merge(df_employees, df_salaries, on="EmployeeID", how="left")

# Merge with bonuses (Left join again)
df_final = pd.merge(df_merge1, df_bonuses, on="EmployeeID", how="left")

# handle missing values: Fill missing bonus with 0
df_final["Bonus"] = df_final["Bonus"].fillna(0)

# Create a calculated field: Total Compensation
df_final["TotalCompensation"] = df_final["Salary"].fillna(0) + df_final["Bonus"]

# Summary: Average total compensation by department
comp_summary = df_final.groupby("Department")["TotalCompensation"].mean().reset_index()

print("Final Emmployee Compensation Datset:")
print(df_final)
print("\nAverage Total compensation by Department:")
print(comp_summary)


