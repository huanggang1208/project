count = 0


def hanoi(n, one, two, three):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, one, three))
        count += 1
    else:
        hanoi(n-1, one, three ,two)
        print("{}:{}->{}".format(n, one, three))
        count += 1
        hanoi(n-1, two, one, three)


hanoi(3, "a", "b", "c")
print(count)






