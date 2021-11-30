# 这个就是全局变量
num = 10


def demo1():
    print("全局变量是%d" % num)


def demo2():
    print("这次的全局变量还是%d"% num)


demo1()
demo2()
