import numpy as np

arr = np.array([1,2,3,4,5,6])

                # The where method

# x = np.where(arr == 4)
# print(x)
                # Find Indexes Of All ODD Numbers In Array

# x = np.where(arr%2!=0)
# print(x)

                #Search Sorted

arr = np.array([5,1,3,4,2,6])
# x = np.searchsorted(arr,2)
# print(x)

#searchsorted will sort the array and then print the index where the element
# is present

# arr = np.array([6,7,8,9])
# x = np.searchsorted(arr,7,side='right')
# print(x)

#optional directions can be given to begin the search

                #Search For Multiple Values

# arr = np.array([1,2,3,4,5])
#
# x = np.searchsorted(arr , [4,5])
#
# print(x)

# Output will be [3,4] as 4 and 5 are present on index 3 and 4