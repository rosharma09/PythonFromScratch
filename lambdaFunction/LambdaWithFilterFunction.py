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



#filter function takes a function and sequence as an input and returns a sequence of elements satisfying the function

#define a function which will return true for even/odd numbers

# for even

def is_even(n):
    return n % 2 == 0

# for odd

def is_odd(n):
    return n % 2 != 0


evenList = list(filter(is_even,lst))
oddList = list(filter(is_odd,lst))

print('The list of even number is: {}'.format(evenList))
print('The number of even number found in list {} is : {}'.format(lst,len(evenList)))

print('The list of odd number is: {}'.format(oddList))
print('The number of odd number found in list {} is : {}'.format(lst,len(oddList)))


