def demo1():
    # 定义一个局部变量
    num = 10

    print("在demo1中的局部变量是 %d" % num)


demo1()


def demo2():
    # print("%d" % num)
    pass


# 在函数内部定义的变量，在外部不能使用
# print("%d" % num)
demo2()
