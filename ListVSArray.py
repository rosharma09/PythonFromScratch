import array as arr

vals = arr.array('i' , [12 , -34, 122, 45, 56])
print(vals)

# functions associated with arrays

# 1.  to get the address and size of the array

print(vals.buffer_info())

# 2.  print the type

print(vals.typecode)

# print the elements of the error

for i in range(5):
    print(vals[i])

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

# to copy the values of one array in to another array

val = arr.array('i' , [1,2,4,6,7])

for e in val:
    print(e)

val1 = arr.array(val.typecode , (a for a in val))

# print the values of the array using the while loop

i = 0
while i < len(val1):
    print(val1[i])
    i += 1

# put the values of an array of int with there squared value

val2 = arr.array('i' , [12, 45, 56, 11 , 5, 6])
val3 = arr.array(val2.typecode , (v*v for v in val2))

for e in val3:
    print(e)