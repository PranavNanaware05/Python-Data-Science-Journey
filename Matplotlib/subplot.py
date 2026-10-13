import matplotlib.pyplot as plt

# Store the days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Store sales values for each day
sales = [20, 30, 25, 40, 50]

# Store temperature values for each day
temperature = [28, 30, 29, 32, 31]

# Set the overall figure size
plt.figure(figsize=(10, 8))

# Create a subplot: 1 row, 1 column, position 1
plt.subplot(1, 1, 1)

# Create a line chart for sales
plt.plot(days, sales)

# Create a subplot: 2 rows, 1 column, position 1
plt.subplot(2, 1, 1)

# Create a scatter plot for temperature
plt.scatter(days, temperature)

# Display grid lines
plt.grid()

# Display all plots
plt.show()