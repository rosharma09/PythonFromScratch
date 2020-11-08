# to create a function which calculates the square of a number

num = int(input('Enter the number:'))

def sqr(n):
    return n * n

res = sqr(num)

print('The square of {} is {}'.format(num,res))

# we can use lambda function in case we don't want to name and save lines of code

f = lambda a : a * a # NOTE: This should have a single expression

res = f(num)
print(res)


# to add two numbers

add = lambda a,b : a + b

addition = add(10,20)
print(addition)