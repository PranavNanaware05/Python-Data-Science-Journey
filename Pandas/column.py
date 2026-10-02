import pandas as pd

# Create a dictionary containing employee details
data = {
    "Name": ["pranav", "Amit", "rahul", "Sneha"],
    "Age": [21, 22, 23, 24],
    "Salary": [20000, 30000, 21000, 40000]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print(df)

# Add a new Department column
df["Department"] = ["IT", "HR", "IT", "Sales"]

# Display the DataFrame with the Department column
print(df)

# Create a new bonus column with 10% of each employee's salary
df["bonus"] = df["Salary"] * 0.10

# Display the DataFrame with the bonus column
print(df)

# Update salary to 31000 for employees earning less than 30000
df.loc[df["Salary"] < 30000, "Salary"] = 31000

# Display the DataFrame after updating salaries
print(df)

# Update salary to 33000 for the employee whose age is 22
df.loc[df["Age"] == 22, "Salary"] = 33000

# Display the DataFrame after the second salary update
print(df)

# Remove the bonus column from the DataFrame
# axis=1 means a column, and inplace=True modifies df directly
df.drop("bonus", axis=1, inplace=True)

# Display the final DataFrame
print(df)