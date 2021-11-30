try:
    # 需要正常执行的代码
    num = int(input("输入一个整数："))

    result = 8 / num
    print(result)

# 错误的类型就是代码抛出的错误的第一个单词
except ZeroDivisionError:
    print("除0错误")

# 未知错误捕获的固定语法
except Exception as result:
    print("未知错误%s" % result)

else:
    print("尝试成功")

finally:
    print("无论怎么样都会成功执行")

print('-' * 40)