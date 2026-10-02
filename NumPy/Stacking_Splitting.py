import numpy as np

a = np.array([10, 20, 30])

b = np.array([50, 60, 70])

# Stack two arrays vertically (one below another)
print("Vertical Stack:", np.vstack((a, b)))  # Vertical stack

# Stack two arrays horizontally (side by side)
print("Horizontal Stack:", np.hstack((a, b)))  # Horizontal stack


# Splitting
arr = np.array([1, 2, 3, 4, 5, 6])

# Split the array into 3 equal parts
print("Split:", np.split(arr, 3))