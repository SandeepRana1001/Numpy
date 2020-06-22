import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

            #Joining 1D Array

# arr = np.concatenate((arr1,arr2))
# print(arr)

            #Join 2D Array

# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([['Apple','Mango','Grapes'],['Tomato','Potato','Onion']])
# arr = np.concatenate((arr1,arr2),axis=1)
# print(arr)

#Here Axis=1 means join arrays along rows
#Axis = 0 is by default means join along columns


             #Joining Using Stack Function
# arr = np.stack((arr1,arr2),axis=1)
# print(arr)

             #Joining Using Stack Function along rows
# arr = np.hstack((arr1,arr2))
# print(arr)

             #Joining Using Stack Function along columns
# arr = np.vstack((arr1,arr2))
# print(arr)
# This Is By Default


             #Joining Using Stack Function along height(depth)
arr = np.dstack((arr1,arr2))
print(arr)

