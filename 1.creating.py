import numpy as np

                # List

list = ["One" , "Two" , "Three"]

                # Passing List In Numpy array

# arr = np.array(list)

        # O D Array or Single Value Array or Scalar Array

# arr = np.array(42)

        # 1 D Array  or Uni Dimensional Array

# arr = np.array(list)

        # 2 D Array has 1D array as its elements

# arr = np.array([[1,2,3] , list])


        # 3 D Array has 2D array as its elements

arr = np.array([[[1,2,3], list , [4,5,6]]])

# print(arr)

            #Check Type Of Array

# print(type(arr))

            # Check Dimension Of Array

# print(arr.ndim)

            # Change Dimensions

arr  = np.array([1,2,3,4,5] , ndmin = 5)

print(arr)

print(arr.ndim)
