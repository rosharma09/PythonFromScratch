import random

i , tryCount = 1, 6

name = input("Please Enter your Name:")


print("Welcome "+ name + "!!")
print("I would like to play a game with you ;) ")

ranNum = random.randint(1,20)
# random number

while i <= tryCount:
    num = int(input("Take a guess between 1 and 20"))

    if num == ranNum:
        print("Woah you have guessed the number in "+str(i)+"guess(s)")

    elif num < ranNum:
        print("The guess is lower than the number i'm thinking of")

    elif num > ranNum:
        print("The guess is higher than the number i'm thinking of")

    i += 1

print("Oops !! you lost")


# usage of break: to break the execution and come out of the loop
# continue: it will continue the next iteration of the loop
# pass: can be used in function, condition block, classes in case when we are not sure about the content of the following

def fun1():
    pass

if 1 < 10:
    pass

