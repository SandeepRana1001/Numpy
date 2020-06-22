import numpy as np

arr = np.array(["Apple","Mango","Banana","Grapes","Orange"])
arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

        # arr[start:end:steps]

# print(arr[1:3])

        # arr[start:all]  if end is missing it means fetch all

# print(arr[1:])

        # arr[0:end]  if start is missing it means start fetching from 0

# print(arr[:3])

        # Negative Slicing

        #start from index 3 from last ie index 3 to index 1 to last ie index 5


# print(arr2[-3:-1])


        #Steps  Returns  elements between start and end

        #start : end : steps

# print(arr2[1:5:2])


           #Slicing In 2D

myarr = np.array([[1,2,3,4,5],["Apple","Mango","Banana","Grapes","Orange"]])
# print(myarr[1,1:4])

#From Second Row Fetch Data From First Index to Fourth Index


           # Return Element From Both Array

# print(myarr[0:2,2])
#Returns 2 nd index i.e third element from both array


           # Return Element From Both Array , this will return 2D array

print(myarr[0:2,1:4])
#Returns 2 nd index i.e third element from both array
