a = 10
b = 4
c = 1

if (a > b and a > c):
    print('The greatest number is a')
    if(a > 5):
        print('Greater than 5')
    else:
        print('Not great')
elif(b > a and b > c):
    print('The greatest number is b')
else:
    print('The greatest number is c')