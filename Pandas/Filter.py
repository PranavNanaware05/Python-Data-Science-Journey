import pandas as pd

# Create a dictionary containing employee details
data = {
    "Name": ["Pranav", "Amit", "Rahul", "Sneha"],
    "Age": [22, 23, 24, 21],
    "city": ["pune", "satara", "sangali", "dhule"],
    "Salary": [20000, 30000, 40000, 50000]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print(df)

# Check which employees are older than 22
print(df['Age'] > 22)

# Display employees whose salary is greater than 30000
print(df[df['Salary'] > 30000])

# Print a separator line
print("=====================")

# Display employees whose age is greater than 22
# AND whose salary is greater than 30000
print(df[(df['Age'] > 22) & (df["Salary"] > 30000)])