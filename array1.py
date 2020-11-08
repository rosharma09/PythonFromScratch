from array import *

arr = array('i' , []) # define an empty array

# to get the length of the array

len = int(input("Enter the length of the array:"))

for n in range(len):
    x = int(input("Enter the next value:"))
    arr.append(x)

print(arr)

toFind = int(input("Please enter the value you want to find in the array:"))

# to find the index value of the element in the array

index = 0

for val in arr:
    if toFind == val:
        print("The element " + str(toFind)+ " is found at the index ["+str(index)+"]")
        break
    else:
        print("element not found")
    index += 1

# to use in-built function to find the index of the value

print("The element " + str(toFind)+ " is found at the index ["+str(arr.index(toFind))+"]")


