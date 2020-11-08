for i in range(4):
    for i in range(4):
        print("# " , end = "")
    print()


# to print a triangle

for i in range(5):
    for j in range(i+1):
        print("* ", end = "")
    print()

# to print a reverse triangle

for i in range(4):
    for j in range(4-i):
        print("* ", end = "")
    print()

# print the pattern for numbers

for i in range(4):
    for j in range(4-i):
        print(j+i+1 , end = "")
    print()

for i in range(4):
    for i in range(4-i):
        print(4-i-j , end = "")
    print()


for i in range(4):
    for i in range(4-i):
        print()