import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha"],
    "Age": [24, np.nan, 27, 23],
    "Salary": [30000, 40000, np.nan, 35000],
    "City": ["Pune", "Mumbai", "Satara", np.nan]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())
print(df.isna())

print(df[df["Age"].notnull()])
print(df)

df["Age"]=df["Age"].fillna(25)


df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df)