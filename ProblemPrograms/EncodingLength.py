str = "aaaabbbbccdddd"

def encodeLength(InputStr):

    if InputStr == None:
        return None

    counter = 0

    for i in str:
        if str[i] == str[i+1]:
            counter += 1
            opStr = str(counter) + str[i]
        elif str[i] != str[i+1]:
            counter = 0






encodeLength(str)