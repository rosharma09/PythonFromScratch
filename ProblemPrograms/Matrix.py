from array import array

from numpy import *

# this program is to illustrate matrix operations

array = array([
    [12,34,56],
    [56,234,56],
    [22,67,89]
])

print(array)
print(array.dtype)

m1 = matrix(array)
print(m1)
print(m1.dtype)

print(m1.diagonal())
# create a matrix using the matrix function

m2 = matrix('1 2 3 ; 4  5 6 ; 7 8  12 ')
print(m2)
print(m2.diagonal())
print(m2.max())
print(m2.min())