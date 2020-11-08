# this is a simple calculator

from math import sqrt , pow

# take the values from the user

x = int(input("Enter 1st Number:"))
print(type(x))
y = int(input("Enter the 2nd Number:"))
print(type(y))

res = x + y

print(type(res))

print("The result is:" +str(res))

# find the square root

num = input("Enter the number")

print("The sqaure root of "+num+" is " + str(sqrt(int(num))))

char = input('Enter a char:')[0]
print(char)

# you can use the eval function to evalute the expressions as input

result = eval(input('Enter the expression:'))
print(result)