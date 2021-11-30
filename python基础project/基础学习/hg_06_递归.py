# 递归方式计算阶乘
def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n - 1)


number = int(input("请输入一个整数："))
result = factorial(number)
print("%d 的阶乘是%d" % (number, result))


# 迭代方式计算阶乘
def recursion(n):
    new_result = n
    for i in range(1, n):
        new_result *= i
    return new_result


number = int(input("请输入一个整数："))
result2 = recursion(number)
print("%d 的阶乘是%d" % (number, result))