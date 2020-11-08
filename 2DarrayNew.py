from numpy import *

array1 = array([
    [12,34,45],
    [32,56,78],
    [1,3,5]
])

array2 = array([
    [12,34,45],
    [32,56,78],
    [1,3,5]
])

print(array1)

# inbuilt functions for multi dimensional arrays

print(array1.dtype) #to print the data type of the array
print(array1.ndim) #to get the dimension of the array
print(array1.shape) #to return the number of rows and columns

res = array1 + array2
print(res)

# to print the number of elements in the matrix

print(res.size)

# to create a 2D array from a 1D array

arrayNew = array([1,2,3,4,5,6])
arrayNew2D = arrayNew.reshape(2,3) # the reshape function can be used to convert a single dimension array into multi dim array
print(arrayNew2D)

arrayNew3D = arrayNew.reshape(2,1,3)
print(arrayNew3D)

# to create a 1D array from 2D array we can use flatten function

a = array([
    [13,22,43,57,96,227],
    [23,45,567,889,12,4]
])

flattenArray = a.flatten()
print(flattenArray)

# create a 3D array out of the 1D array

array3d = flattenArray.reshape(4,1,3)
print(array3d)