# 20250921 Daily Python Practice - Data Analyst
# Task : Perform data transformations, create calculated fields, and filter data for insights

import pandas as pd

# Sample employee dataset
data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"], 
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT"], 
    "Salary": [55000, 60000, 50000, 52000, 65000, 70000],
    "Bonus": [5000, 7000, 3000, 3200, 8000, 8500], 
    "YearsAtCompany": [2,5,3,4,6,7]
}

df = pd.DataFrame(data)

# Create a calculated column: Total Compensation
df["TotalCompensation"] = df["Salary"] + df["Bonus"]

# Create a flag for senior employees (>=5 years)
df["SeniorEmployee"] = df["YearsAtCompany"] >= 5

#Fileter: Only senior employees in Sales
senior_sales = df[(df["Department"] == "Sales") & (df["SeniorEmployee"] == True)]

# Group: Average total compensation by department
comp_summary = df.groupby("Department")["TotalCompensation"].mean().reset_index()

print("Employee Data with Transformations:")
print(df)
print("/nSenior Sales Employees:")
print(senior_sales)
print("/nAverage Total Compensation by Department:")
print(comp_summary)












