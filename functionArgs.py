# types of arguments:

def fun1(name = "Random" , age = 18):
    print(name)
    print(age)

# 1. postinal arguments
fun1("Rohan" , 25)

# 2. Keyword argument
fun1(age = 15 , name = "Mohan")

# 3. Default argument
fun1("Rishab")
fun1()

# variable length argument

# function with two arguments
def sumAll(a, *b):
    print("The value of the 1st Argument passed is:" +str(a))
    print("The type of the 1st Argument passed is:" +str(type(a)))

    print()

    print("The value of the 2nd Argument passed is:" +str(b))
    print("The type of the 2nd Argument passed is:" +str(type(b)))


    sum = a
    for i in b:
        sum = sum + i
    return sum

res = sumAll(10,20,12,1,6)
print("The sum of all the passed values is:" +str(res))

# sum all function with single argument:

def sumAll1(*a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

res = sumAll1(12,23,456,678)
print(res)

def functionAdd(x,y):
    sum = x + y
    return sum

res = functionAdd(10,20)
print(res)


def isPrime(num):
    if(num == 1):
        return False
    for i in range(2,num):
        if(num % i == 0):
            return False
    else:
        return True

isNumberPrime = isPrime(num = 13)
print(isNumberPrime)


