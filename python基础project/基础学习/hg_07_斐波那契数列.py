# 使用迭代实现
def fab(n):
    a1 = 1
    a2 = 1
    a3 = 1

    if n < 1:
        print("输入错误")
        return -1

    while (n - 2) > 0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1

    return a3


result = fab(40)

if result != -1:
    print("总共有%d对兔子诞生！" % result)


# 用递归来实现
# 用递归来实现的时候，如果数据过大，反而会造成效率低下
def fab(n):
    if n < 1:
        print("输入错误")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)


new_result = fab(5)
if new_result != -1:
    print("总共有%d对兔子诞生！" % new_result)
