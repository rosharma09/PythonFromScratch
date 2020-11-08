a = 2
b = 4

# method 1 - using a third variable

temp = a
a = b
b = temp

print(a)
print(b)

# method 2 - using the below formula

a = a + b # 2 + 4 = 6
b = a - b # 6 - 4 = 2
a = a - b # 6 - 2 = 4

print(a,b)

# method 3 - using the python syntax of assignment a,b = b,a [ROT_TWO() - rotates the value]

a,b = b,a
print(a,b)

# method 4 - using the XOR operator[No extra bits are used]

a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)