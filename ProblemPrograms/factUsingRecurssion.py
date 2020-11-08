# we are going to implement factorial using recursion

userInput = int(input('Enter the value: '))

def factRecursive(n):

    if(n == 1):
        return 1

    return n * factRecursive(n-1)

res = factRecursive(userInput)

print('{}! : {}'.format(userInput,res))

