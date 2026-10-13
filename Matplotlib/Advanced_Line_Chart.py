import matplotlib.pyplot as plt

# Create a list of months for the X-axis
month = ["jan", "feb", "mar", "Apr"]

# Sales data for the year 2025
sale_2025 = [100, 120, 150, 140]

# Sales data for the year 2026
sale_2026 = [110, 130, 160, 180]

#plt.plot(month,sale_2026,linestyle="--")
# Plot the 2025 sales with circular markers and a legend label
plt.plot(month, sale_2025, marker="o", label="2025")

# Plot the 2026 sales with circular markers and a legend label
plt.plot(month, sale_2026, marker="o", label="2026")

# Plot the 2026 sales again with 50% transparency
# alpha=0 means completely transparent
# alpha=1 means completely opaque
plt.plot(month, sale_2026, alpha=0.5)

# Set the limits of the X-axis
plt.xlim(0, 4)

# Set the limits of the Y-axis
plt.ylim(80, 200)

# Add text annotation at the April sales point
plt.text("Apr", 180, "Highest Sale")

# Rotate X-axis labels by 45 degrees
plt.xticks(rotation=45)

# Add a title to the chart
plt.title("Sale comparison")

# Add a label to the X-axis
plt.xlabel("Month")

# Add a label to the Y-axis
plt.ylabel("Sales")

# Display the legend
plt.legend()

# Display grid lines
plt.grid()

# Display the chart
plt.show()