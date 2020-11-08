x = ['Rohan' , 'Sharma' , 25 , 'QA' , 8.98]

for i in x:
    print(i)

str = 'ROHAN'

for i in str:
    print(i)

for i in {12 , 34, 45, 12, 12}:
    print(i)

for i in (12 , 34, 56, 12, 34):
    print(i)

# print even numbers from 1-100

for i in range(2,101,2):
    print(i)
# print the number in reverse order

for i in range(100 , 0 , -10):
    print(i)

# print a series from 1 - 20 excluding number divisible by 5

for i in range(1 , 21):
    if(i % 5 != 0):
        print(i)


# print number from 1 - 50 excluding number divisible by 3 and 5

for i in range(1 , 51):
    if i % 3 == 0 and i % 5 ==0:
        continue
    print(i)
