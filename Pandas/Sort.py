import pandas as pd
data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha"],
    "Age": [24, 21, 27, 23],
    "Salary": [30000, 40000, 25000, 35000]
}

df = pd.DataFrame(data)
print(df.iloc[0:2,1:3])