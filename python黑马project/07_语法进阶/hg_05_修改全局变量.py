# 这个就是全局变量
num = 10


def demo1():
    # 希望修改全局变量的值--使用global声明一下变量即可
    global num
    
    num = 99
    print("全局变量是%d" % num)


def demo2():
    print("这次的全局变量还是%d"% num)


demo1()
demo2()
