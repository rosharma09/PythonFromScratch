# calculate factorial of a number

number = int(input('Enter the value'))

def fact(n):

    fact = 1

    for i in range(1 , n+1):
        fact = fact * i

    return fact


result = fact(number)

print("{}! = {}".format(number,result))