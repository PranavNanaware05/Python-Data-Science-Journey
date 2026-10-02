import pandas as pd

data = {
    "Name": ["Pranav", "Rahul", "Amit", "Sneha"],
    "Age": [22, 23, 24, 22],
    "City": ["Pune", "Mumbai", "Satara", "Pune"],
    "Salary": [30000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)
print(df)

print(df["Name"])
print(df[["Name","Age","Salary"]])
print(df.loc[0])
print(df.loc[2:3])
print("==================")
print(df.loc[1:3,["Name"]])
print(df.iloc[1])