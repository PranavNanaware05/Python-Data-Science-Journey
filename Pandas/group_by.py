import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Kiran"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Age": [24, 21, 27, 23, 26],
    "Salary": [30000, 40000, 25000, 35000, 45000]
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Salary"].min())

print(df.groupby("Department")["Salary"].max())

print(df.groupby("Department")["Name"].count())
print(df.groupby("Department")["Name"].size())

print(df.groupby("Department").agg({
    "Age":"mean",
    "Salary":"max"
}))


print(df.groupby("Department")["Salary"].agg(["min","max","mean"]))

print(df.groupby("Department").agg(
    {
        "Age":"mean",
        "Salary":"sum"
    }
).reset_index())

print(df.groupby("Department").agg({
    "Age":["min","max"],
    "Salary":["min","max"]
}))
