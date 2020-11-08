for i in range(4):
    for j in range(4-i):
        print(4 - i - j , end = "")
    print()


for i in range(4):
    for j in range(i+1):
        print(j+1 , end = "")
    print()

# print the pattern of alphabets

for i in range(4):
    for j in range(i + 1):
        print(chr(65 + j) + " " , end= "")
    for k in range(4 - i):
        print(chr(80 + k) + " " , end= "")
    print()
