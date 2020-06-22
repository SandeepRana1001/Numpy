from numpy import random

        #Generate Random Integer
# x  = random.randint(100)

        # Generate Random Float Between 0 and 1
# x = random.rand()

        # Generate Random Array 1D
# x = random.randint(100,size=(5))

#Here Size Is The Size Of Array

        # Generate Random Array 2D

# x = random.randint(100,size=(5,5))

        #Shape Of Array 1D
# x = random.rand(5)

        #Shape Of Array 2D
# x = random.rand(5,5)

         #The Choice Method
x= random.choice([1,2,3,4])
# print(x)

# The choice() method allows you to generate a random
# value based on an array of values.

# The choice() method takes an array as a parameter and randomly returns
# one of the values.

            #2D Array Using Choice

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)