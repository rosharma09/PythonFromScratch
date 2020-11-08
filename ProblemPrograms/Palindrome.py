# palindrome check

num = int(input('Enter the number:'))

def isPalindrome(n):
    temp = n
    sum = 0
    while n != 0:
        rem = n % 10
        n = int(n/10)
        sum = sum * 10 + rem

    if temp == sum:
        return True
    else:
        return False

res = isPalindrome(num)

if res:
    print('The entered number {} is a palindrome'.format(num))
else:
    print('The entered number {} is not a palindrome'.format(num))