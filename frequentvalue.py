#Numpy program to find most frequent value in an array

import numpy as np
# to store 50 random numbers from 1 to 8 in nparray
x = np.random.randint(1, 8, 50) #nparray consists of 50 random numbers from 1 to 8 
print(x)
#to find frequently occured value in the above randomly generated array
print("bincount() returns: ",np.bincount(x)) #returns the count of each value in an array of non-negative integers and return an array with the count at the appropriate index
print("Most frequent value in the array x: ")
print(np.bincount(x).argmax())
#np.argmax() returns the index of the maximum value in an array

'''
OUTPUT:
[7 7 3 6 1 4 4 2 1 3 7 4 1 1 2 4 2 5 4 5 6 3 2 5 1 4 7 7 4 4 4 2 6 3 2 2 3
 3 6 2 3 2 1 4 6 1 2 1 7 2]
bincount() returns: [ 0  8 11  7 10  3  5  6]
Most frequent value in the array x: 
2
'''
