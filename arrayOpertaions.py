import numpy as n

a = n.array([5,7,2,1])
temp = a*a
print(temp)
temp = (n.sqrt(temp))
print(temp)

# add a fixed number to all the values in the array

a = a + 5
print(a)

# use the trignometry functions

print(n.sin(a))
print(n.log(a))

# use the max,min etc

print(n.max(a))
print(n.min(a))
print(n.sum(a))
print(n.sort(a))

print(n.concatenate([a,a]))

# to copy the content of one array into another array

a1 = n.array([12,34,56,678])
a2 = a1
print(a1)
print(a2)

print(id(a1),id(a2))

a2 = None

print(a2)

a2 = a1.copy()
print(a2)

