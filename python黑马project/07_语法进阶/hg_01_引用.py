def test(num):

    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))


# 定义一个数字变量
a = 10

# 数据的内存地址本质上就是一个数字
print("a 的变量保存的数据的内存地址是 %d" % id(a))

# 调用test函数
test(a)
