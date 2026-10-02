import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Kiran"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Age": [24, 21, 27, 23, 26],
    "Salary": [30000, 40000, 25000, 35000, 45000]
}

df = pd.DataFrame(data)

print(df["Salary"].sum())
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].median())
print(df["Name"].count())
print(df["Salary"].agg(["sum","mean","min","max"]))
print(df["Age"].agg(["mean","min","max"]))
print(df.agg({
    "Age":["mean","max"]
}))
print(df.agg({
    "Age":["min","mean"],
    "Salary":["max","sum"]
}))
print(df["Salary"].std())