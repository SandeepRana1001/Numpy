import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

    # Shape Of the array is its dimension

# NumPy arrays have an attribute called shape that returns a tuple with
# each index having the number of corresponding elements.

# print(arr.shape)

# Output = > (2,5)
# Because the array has 2 rows or 2 arrays and each containing 5 elements


            # Tips and Tricks

arr = np.array([1,2,3,4] , ndmin=5)

print(arr.shape)

# As no other elements are presented python assigns single value to the missing
# rows which makes it 1
