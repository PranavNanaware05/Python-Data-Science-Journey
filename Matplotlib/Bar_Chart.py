import matplotlib.pyplot as plt

# List of student names for the X-axis
students = ["Amit", "Rahul", "Sneha", "Pranav"]

# Marks obtained by each student
marks = [75, 83, 68, 90]

# Create a vertical bar chart
# alpha=1 means the bars are completely visible
# width=0.5 controls the width of each bar
# label="marks" gives a name to the bar chart for the legend
bars = plt.bar(
    students,
    marks,
    alpha=1,
    width=0.5,
    label="marks"
)

# Add a title to the chart
plt.title("Student Marks")

# Add a label to the X-axis
plt.xlabel("Student Name")

# Add a label to the Y-axis
plt.ylabel("Marks")

# Create a horizontal bar chart
# Uncomment this line if you want horizontal bars
# plt.barh(students, marks)

# Display the legend
plt.legend()

# Add custom text above Pranav's bar
# 3 = X-position of Pranav's bar
# 90 = Y-position
# "Topper" = text to display
plt.text(3, 90, "Topper")

# Add grid lines to the chart
# Uncomment to enable the grid
# plt.grid()

# Display the exact value on top of each bar
plt.bar_label(bars)

# Rotate X-axis labels by 45 degrees
plt.xticks(rotation=45)

# Display the chart
plt.show()