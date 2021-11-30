try:
    num = int(input("输入一个整数："))

    result = 8 / num
    print(result)

# 错误的类型就是代码抛出的错误的第一个单词
except ZeroDivisionError:
    print("除0错误")

# 未知错误捕获的固定语法
except Exception as result:
    print("未知错误%s" % result)