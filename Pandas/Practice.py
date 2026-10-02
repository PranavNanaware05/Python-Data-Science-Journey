import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Kiran", "Priya", "Rohan"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "Finance", "Finance"],
    "Age": [24, 21, 27, 23, np.nan, 26, 29],
    "Salary": [30000, 40000, np.nan, 35000, 45000, 50000, 55000],
    "JoiningDate": [
        "2025-01-15", "2025-03-20", "2024-12-10",
        "2025-06-25", "2025-02-10", "2024-11-15", "2025-04-01"
    ]
}

df = pd.DataFrame(data)

df["JoiningDate"]= pd.to_datetime(df["JoiningDate"])


print(df.groupby("Department").agg({
    "Name":"count",
    "Age":"mean",
    "Salary":["min","max"]
}))