# There is no concept of call by value / call by reference in python

def update(x):
    print("The id of passed value is :" + str(id(x)))
    # update the value of x
    x = 10
    print("The id of updated value of x is :" +str(id(x)))
    print(x)


a = 20
print("The id for a is:" +str(id(a)))
update(a)


def updateList(lst):
    print(id(lst))
    lst[1] = 100
    print(id(lst))

lst = [12,34,56]
print(lst)
updateList(lst)
print(lst)

