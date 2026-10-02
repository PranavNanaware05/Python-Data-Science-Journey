import pandas as pd

# Create a dictionary containing employee data
data = {
    "Name": ["Pranav", "Rahul", "Amit", "Sneha", "Rohit", "Priya"],
    "Age": [22, 23, 24, 22, 25, 23],
    "Salary": [30000, 35000, 28000, 32000, 40000, 38000]
}

# Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print(df)

# Display the first 2 rows of the DataFrame
print("First rows:")
print(df.head(2))

# Display the last 2 rows of the DataFrame
print("Last rows:")
print(df.tail(2))

# Display the shape of the DataFrame (rows, columns)
print("Shape:", df.shape)

# Display all column names
print("Column names:", df.columns)

# Rename the Salary column to monthly_salary
df.rename(columns={'Salary': 'monthly_salary'}, inplace=True)

# Display the DataFrame after renaming the column
print("After renaming column:")
print(df)

# Display DataFrame information such as column names, data types, and null values
df.info()

# Display statistical summary of numerical columns
print(df.describe())