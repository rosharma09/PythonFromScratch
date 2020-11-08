from numpy import *

# this program is to illusrtate the different ways of creating array using numpy

# method 1: using the array function --> we can give the array values and provide the type

intArray = array([1,2,3,4] , int)
print(intArray)


floatArray = array([1,2,3,4] , float)
print(floatArray)

charArray = array(['a','b','c'])
print(charArray)

# method2: using the linspace function --> we can create an array by providing the start and end of the array
# and specify the number of parts

splitArray = linspace(0,15,16) # sytax : linspace(start,end,splitCount)
print(splitArray)

# method3: using the logspace function --> we can create an array with the logs of the range and divided into equal parts

logArray = logspace(1,40,10)
print(logArray)
print('%.2f' %logArray[0])

# method3: arange function --> to specify an array of range of numbers
rangeArray = arange(0,10,2)
print(rangeArray)

# mehtod4: to create an array with zeros

zeroArray1 = zeros(5, int)
print(zeroArray1)

# method5: to create an aray of 1s
onesArray = ones(5)
print(onesArray)