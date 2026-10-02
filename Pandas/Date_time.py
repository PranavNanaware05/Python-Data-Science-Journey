import pandas as pd

# Create a dictionary containing employee names and joining dates
data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha"],
    "JoiningDate": [
        "2025-01-15",
        "2025-03-20",
        "2024-12-10",
        "2025-06-25"
    ]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Convert JoiningDate column from string to datetime format
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

# Extract the year from JoiningDate
df["year"] = df["JoiningDate"].dt.year

# Extract the month number from JoiningDate
df["month"] = df["JoiningDate"].dt.month

# Extract the day from JoiningDate
df["day"] = df["JoiningDate"].dt.day

# Extract the day name, such as Monday, Tuesday, etc.
df["day_Name"] = df["JoiningDate"].dt.day_name()

# Extract the month name, such as January, February, etc.
df["MonthName"] = df["JoiningDate"].dt.month_name()

# Display employees who joined after January 1, 2025
print(df[df["JoiningDate"] > "2025-01-01"])

# Display employees who joined between January 1 and March 31, 2025
print(df[df["JoiningDate"].between("2025-01-01", "2025-03-31")])

# Sort employees by JoiningDate from newest to oldest
df=df.sort_values("JoiningDate", ascending=False)

# Display the final DataFrame
print(df)