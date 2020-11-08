# this program is to illustrate the usage of keyworded variable length argument

# note : to specify that we are using a keyworded variable length argument, we use **

def user(name,**data):
    print(name , type(name))
    print(data,type(data))

    # print the key value pair
    for i,j in data.items():
        print(i,j)

user('Rohan',age = 25,city = 'Bengaluru',number = 9741374660, designation = 'QA Engineer')