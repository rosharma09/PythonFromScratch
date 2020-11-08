i = 1

while i <= 3:
    print('Hello' , end = "")
    j = 1
    while j <=3:
        print('World', end = "")
        j += 1
    print()
    i += 1

# to print the number from 1-100 excluding numbers that are divisible bu 3,5

i = 1

while i <= 100:
    if(i % 3 == 0 or i % 5 ==0):
        i += 1
        continue

    else:
        print(i)
    i += 1

i = 1
j = 5
while i <= 5:
    print("*" , end = "")
    while(j >= 1):
        print("*" , end = "")
        j -= 1
    print()
    i += 1