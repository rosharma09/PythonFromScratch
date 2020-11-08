# program to print the fibonacci series upto a given value

LessThanN = int(input('Please enter the value under which you want to print the fibonacci series: '))

def fibo(n):

    a = 0
    b = 1
    c = 0

    if n == 1:
        print(a)

    elif n <= 0:
        print('Not a valid value!!!')

    else:
        print(str(a) + " " , end = "")
        print(str(b) + " " , end = "")

        for i in range(2,n):
            c = a + b
            a = b
            b = c

            if c >=n:
                break
            else:
                print(str(c) + " ", end="")

fibo(LessThanN)