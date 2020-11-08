import time
import math as m

def is_Prime_v1(num):
  """return true if 'num' is prime. return false in case 'num' is not a prime """
  if num == 1:
      return False # 1 is not a prime
  for n in range(2,num):
      if num % n == 0:
          return False # number is divisible and hence not a prime
      else:
          return True

def is_prime_v2(num):
    """return true if 'num' is prime. return false in case 'num' is not a prime """
    if num == 1:
        return False
    for n in range(2, m.floor(m.sqrt(num))):
        if num % n == 0:
            return False
        else:
            return True


t0 = time.time()
for i in range(1, 100000):
    res = is_Prime_v1(i)
    print("Is " + str(i) + " Prime:" + str(res))
t1 = time.time()

print("The time taken is :" + str(t1-t0))


t2 = time.time()
for i in range(1, 100000):
    res = is_prime_v2(i)
    print("Is " + str(i) + " Prime:" + str(res))
t3 = time.time()

print("The time taken is :" + str(t1-t0))
print("The time taken is :" + str(t3-t2))

