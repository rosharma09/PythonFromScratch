from numpy import *

arr = array([1,2,3.2,5])
print(arr.dtype)
print(arr)

# use of linspace --> usage --> linspace(start,stop,splitIntoParts)

arr1 = linspace(0,15,16)
print(arr1)

# use of arange --> usage --> arange(start, end , step)

arr2 = arange(0 , 15, 3)
print(arr2)

# use of logspace --> usage --> logspace(start, stop , difference in the log value)

arr3 = logspace(0 , 40 ,5)
print(arr3)
print('%.2f' %arr3[4])

from array import *
a = array('i',[12,34,45,122,4567,789],[12,34,45,122,4567,789])
print(a)

for arrElement in a:
    print(arrElement)

