import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

                # Reshaping 1D Array To 2D Array

# newarr = arr1.reshape(4,3)


                # Reshaping 1D Array To 3D Array

newarr = arr1.reshape(2,3,2)


                # Tips and Tricks

# print(newarr.base)

# As we know using base return original array if it is not a copy


                #Converting 2D array to 1D array
newarr = arr2.reshape(-1)
print(newarr)