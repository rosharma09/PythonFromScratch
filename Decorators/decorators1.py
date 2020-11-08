# Usage of decorators: to modify the existising functionality of an function

# function to divide two numbers

def div(a,b):
    print(a/b)


def smartDiv(func):
    def innerDiv(a,b):
        if a < b:
            a,b = b,a # reverse the numbers
        return func(a,b)
    return innerDiv

div = smartDiv(div)

div(2,4)
