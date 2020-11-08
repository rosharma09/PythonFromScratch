# we can define a function using def keyword

def add(x,y):
    c = x + y
    return c

def add_sub(x,y):
    c = x + y
    d = x- y
    return c,d

res = add(12,45)
print(res)

res1,res2 = add_sub(122,45)
print(res1, res2)

