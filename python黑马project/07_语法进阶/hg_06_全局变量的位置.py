# 注意在开发中要把全局变量放在开头的位置
# 这样所有的函数都能使用全局变量
# 全局变量
num = 100
# 再定义一个全局变量
name = "黄岗"
# 再定义一个全局变量
title = "全局变量的位置"


def demo():
    print("%d" % num)
    print("%s" % name)
    print("%s" % title)


demo()

# # 再定义一个全局变量
# title = "全局变量的位置"
