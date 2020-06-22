import numpy as np

arr = np.array([1,2,3,4,5])

#Filtering Is Used To Get A New Array Out Of Original Array using boolean values

# x = [True,False,True,False,True]
# newarr = arr[x]
# print(newarr)

#Output will be [1 3 5] because the new array has
#index 0 , index 2 , index 4 as true and other as false.


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create A Filter Array With Even Values Only (Short Method)

# filter_arr = arr%2==0
#
# newarr = arr[filter_arr]
#
# print(newarr)

            # Create A Filter Array With Even Values Only (Long Method)

filter_arr=[]       # declaring a array to for using append method

for element in arr:
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(newarr)


# Use Long Method or Short Method According To Your Requirement