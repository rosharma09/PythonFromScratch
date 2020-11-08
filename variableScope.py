# scope of variable : area within which a variable can be accessed

#define a global variable --> which is accessable throughout the code
globalVar = 10

def fun():
    global globalVar # we are specifying python interpreter that we are using the global variable here
    globalVar = 20
    print(globalVar)

fun()
print(globalVar)

# we can use both local and global varable inside a function

var = 10
print(id(var))

def fun1():
    var = 15
    print(id(var))
    x = globals()['var']
    print(id(x))
    print(var)
    print(x)
    # update the value of global variable
    globals()['var'] = 40

fun1()
print(var)