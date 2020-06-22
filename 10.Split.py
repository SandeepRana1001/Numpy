import numpy as np

arr = np.array([1,2,3,4,5])

                #Split Array

newarr = np.array_split(arr,5)

#Using array_split(array_name,Number of splits) will split the array

# print(newarr)

                #Spliting 2D Array

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# newarr = np.array_split(arr,5,axis=1)

                #Splitting Along height

# newarr = np.hsplit(arr,5)
#
# print(newarr)