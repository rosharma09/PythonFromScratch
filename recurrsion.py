# recurrsion --> function calling itself

import sys

# define a global variable count

count = 0

# in order to set the recurrsion limit

sys.setrecursionlimit(20)

print(sys.getrecursionlimit())

def greet():
    global count
    count += 1
    print("Hello" , count)
    greet()

greet()