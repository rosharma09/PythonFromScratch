from array import *

Arrlen = int(input("Enter the length of the Array:"))

# define an empty array
arr = array('i', [])

for i in range(Arrlen):
    elem = int(input("Enter the next value:"))
    arr.append(elem)

reverseArr = array('i', [])


print(arr[0])

def reverse(a):
    reverseArrayLen = a.len()
    for i in range(reverseArrayLen):
        reverseArr.append(a[len(reverseArr) - 1])
    return reverseArr

res = reverse(arr)
print(res)



