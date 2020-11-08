# program to illustrate filter, map and reduce:

# to use the reduce we need to import the reduce function

from functools import reduce

#Define a list of numbers

inputList = [1500,2500,1200,4800,5400,900,2001,1245,255]

# filter --> filter the values greater than 2000

list1 = list(filter(lambda n: n > 2000 , inputList))
print(list1)

# map --> change the values greater than lesser than 2000 to double of it
list2 = list(map(lambda n : n * 2 , list(filter(lambda n : n < 2000, inputList))))
print(list2)

# reduce --> find the sum of all the values that are lesser than 1000

list3 = reduce(lambda x,y : x + y ,list(filter(lambda n : n < 1000, inputList)))
print(list3)