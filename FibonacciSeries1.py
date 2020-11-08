# print the fibonacci series upto n number

uptoN = int(input('Enter the value upto which you want to print the fibonacci series:'))

def fibo(n):

    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 0:
        print('Not a valid value!!')
    else:
        print(str(a)+" ", end = "")
        print(str(b)+" ", end = "")
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(str(c)+" ", end = "")

fibo(uptoN)