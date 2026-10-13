import matplotlib.pyplot as plt

# Create a list of months for the X-axis
months = ["jan", "feb", "mar", "Apr"]

# Create a list of sales values for the Y-axis
sale = [100, 120, 90, 200.70]

# Create a line chart using months and sales
plt.plot(months, sale)

# Add a title to the chart
plt.title("Monthly Sale")

# Add a label to the X-axis
plt.xlabel("Months")

# Add a label to the Y-axis
plt.ylabel("Sale")

# Add grid lines only along the X-axis
# plt.grid()

# Add grid lines along the X-axis
plt.grid(axis="x")

# Add grid lines along the Y-axis
plt.grid(axis="y")

# Display the legend
plt.legend()

# Display the chart
plt.show()