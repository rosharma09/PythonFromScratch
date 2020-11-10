# this is a sample program to illustrate the usage of decorators

# define a function which calculates the difference of two passed values

def difference(a,b):
    return a - b

# in case the first argument is greater than the second argument the difference comes in negative

# define a decorator which will return the difference in +ve

def differencePositive(func):
    def innerFunction(a,b):
        if a < b:
            # logic to swap the numbers
            temp = a
            a = b
            b = temp
        return func(a,b)
    return innerFunction


# create a relation between the main function and decorator

difference = differencePositive(difference)

res = difference(10,20)
print('The difference is {}'.format(res))


