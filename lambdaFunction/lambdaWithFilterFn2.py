# use the odd/even lambda function expression directly in the filter function

# usgae of lambda function with filter function

import random

# define the range of the random numbers to be selected

lower = 10
upper = 100

# create a list of random numbers numbers

listLen = int(input('Enter the length of the list:'))

# create an empty list
lst = []

for i in range(listLen):
    lst.append(random.randint(lower,upper))

print(lst)

evenList = list(filter(lambda n : n % 2 == 0,lst))
oddList = list(filter(lambda n : n % 2 != 0,lst))

print('The list of even number is: {}'.format(evenList))
print('The number of even number found in list {} is : {}'.format(lst,len(evenList)))

print('The list of odd number is: {}'.format(oddList))
print('The number of odd number found in list {} is : {}'.format(lst,len(oddList)))