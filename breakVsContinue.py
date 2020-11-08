for i in range(1,20,2):
    if i % 3 == 0:
        continue

    if i % 5 ==0:
        break

    print("Hello"+str(i))