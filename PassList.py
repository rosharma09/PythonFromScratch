# pass list as an arg to a fn

# create a function which takes list of numbers as an input and returns the number of even and odd number in the lsit

# define a list
numberList = []
print(type(numberList))

# ask user to enter the length of the lsit

listLength = int(input('Enter the list length: '))


for i in range(0,listLength):
    val = int(input('Enter the next value:'))
    numberList.append(val)

print(numberList)

def count(inputList):
    eCount = 0
    oCount = 0

    for i in inputList:
        if i % 2 == 0:
            eCount += 1
        else:
            oCount += 1

    return eCount , oCount

oddCount , evenCount = count(numberList)
print("Even : {} and Odd : {}".format(evenCount,oddCount))