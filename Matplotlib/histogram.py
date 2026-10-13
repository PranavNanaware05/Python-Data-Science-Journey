import matplotlib.pyplot as plt

# List containing the marks of students
marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 80, 85, 90]

# Create a histogram
# bins=5 divides the marks into 5 intervals (groups)
# edgecolor="black" adds a black border around each bar
plt.hist(marks, bins=5, edgecolor="black")

# Add a title to the histogram
plt.title("Marks Distribution")

# Add a label to the X-axis
plt.xlabel("Marks")

# Add a label to the Y-axis
# Frequency means how many values fall into each interval
plt.ylabel("Frequency")

# Add grid lines to the chart
# Uncomment this line if you want to display the grid
# plt.grid()

# Rotate X-axis labels by 45 degrees
plt.xticks(rotation=45)

# Display the histogram
plt.show()