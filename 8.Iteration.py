import numpy as np
k=0
l=0
m=0
arr = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr3 = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])

            # Iterating 1D Array Using For Loop

# for i in arr:
#     print("Element At Index ",k," Is: ",i)
#     k=k+1

            # Iterating 2D Array Using For Loop

# for i in arr2:
#     print("Elements At Index ",k,"Are: ")
#     for j in i:
#         print("Element At Index[",k,l,"] Is: ", j)
#         l=l+1
#     k=k+1

# To Fetch Each Values From 2D Array We Need 2 Loops

            # Iterating 3D Array Using For Loop

# for i in arr3:
#     for x in i:
#         for y in x:
#             print("Element At Index[",k,l,m,"] Is: ", y)
#             m=m+1
#         l=l+1
#         m=0
#         print("\n")
#     k=k+1


# To Fetch Each Values From 2D Array We Need 3 Loops


        #Iterating Arrays Using nditer()

# for x in np.nditer(arr3):
#     print(x)

#nditer makes it simple to iterate and fetch value from most complicated to most
#simple numpy arrays


        #ndenumerate() helps in mentioning the sequence

for idx , x in np.ndenumerate(arr3):
    print(idx,x)
# It also tells the index number in which element is present