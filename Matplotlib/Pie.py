import matplotlib.pyplot as plt

# List of product names
products = ["Laptop", "Mobile", "Tablet", "Watch"]

# Sales values for each product
sales = [50, 80, 40, 60]

# Specify which pie slice should be separated/exploded
# 0   → normal position
# 0.1 → move the slice slightly outward
explode = [0, 0.1, 0, 0]

# Create the pie chart
plt.pie(
    sales,                  # Values used to calculate slice sizes
    labels=products,        # Names displayed for each slice
    autopct="%1.1f%%",      # Display percentage with 1 decimal place
    explode=explode,        # Separate the Mobile slice
    startangle=90,          # Start the pie chart from 90 degrees
    shadow=True              # Add a shadow effect
)

# Add a title to the chart
plt.title("Pie Chart")

# Add an X-axis label
# Note: pie charts normally don't need X/Y axis labels
plt.xlabel("Sales")

# Add a Y-axis label
# Note: pie charts normally don't need X/Y axis labels
plt.ylabel("Products")

# Add grid lines along the X-axis
# Usually not required for a pie chart
plt.grid(axis="x")

# Make the pie chart circular instead of oval-shaped
plt.axis("equal")

# Display the chart
plt.show()