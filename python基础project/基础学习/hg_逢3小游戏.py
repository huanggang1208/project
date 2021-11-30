for i in range(1, 101):
    if (i % 3 == 0) or (i % 7 == 0):
        print("pass")
    elif (3 == i % 10) or (7 == i % 10):
        print("pass")
    else:
        print(i)
