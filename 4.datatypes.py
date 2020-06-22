import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([[1,2,3,4,5],["Apple","Mango","Banana","Grapes","Oranges"]])

        #Check DataType
            # Data Types In Python
                # i - integer
                # b - boolean
                # u - unsigned integer
                # f - float
                # c - complex float
                # m - timedelta
                # M - datetime
                # O - object
                # S - string
                # U - unicode string
                # V - fixed chunk of memory for other type ( void )
# print(arr.dtype)
# print(arr2.dtype)

        #Assign Datatype To Array

# arr = np.array([1, 2, 3, 4], dtype='i4')
#
# print(arr)
# print(arr.dtype)


# arr = np.array(['a', '2', '3'], dtype='i')

# The Above Line will give an error as 'a' i.e index 0 of array cannot be converted
# to integer as it is a a string

            #Converting Data Type on Existing Arrays

                #Make Copy Of Array using astype and change the datatype

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i') # use i or int both will work
# newarr = arr.astype(int) # use i or int both will work

            # Same Can be done with other datatypes
floatarr = newarr.astype(float)

print(newarr)
print("Datatype of arr",arr.dtype)
print("Datatype of newarr",newarr.dtype)
print("Datatype of Stringarr",floatarr.dtype)