import  numpy as np

# The Main difference between view & copy is

# copy is copy of original data and changes made in copy
# or actual data will not affect it

# view is view of orginal data and changes made in view
#  or actual data will affect it

arr  = np.array([1,2,3,4,5])

                # Copy

# newarr = arr.copy()
#
# arr[1]=102
#
# print(arr)
#
# print(newarr)

# As we can see newarr is not affected by changes as it was a copy
# while in arr the value in index 1 is now 102

            # View

newarr = arr.view()

arr[1]=102

# print(arr)
#
# print(newarr)

# As we can see newarr is affected by changes as it was a view
# and in arr the value in index 1 is now 102


            # Tips and Tricks

# newarr = arr.view()
#
# arr[1]=102
#
# newarr[2]=52
#
# print(arr)
#
# print(newarr)

#Changes Made In View Will Affect The Original Array Too


                # Check if array owns its data

x = arr.copy()

y = arr.view()

# print(x.base)

# print(y.base)

# Base is a attribute in numpy which returns none if array owns the data
# otherwise it refers to original data