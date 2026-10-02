import numpy as np

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Print elements from index 1 to 3
print(arr[1:4])

# Print elements from index 2 to the end
print(arr[2:])

# Reverse the array
print(arr[::-1])

# Print every second element
print(arr[::2])

print("Operations on 2D Array")

# Create a 2D NumPy array
arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Slice first two rows and all columns
print(arr1[:2, :])

# Slice all rows and first two columns
print(arr1[:, :2])

# Slice first two rows and second column only
print(arr1[0:2, 1:2])