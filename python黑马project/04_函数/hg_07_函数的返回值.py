def sum_2_num(num1, num2):
    """两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数的一方计算函数的结果
    return result


# 可以使用变量来接收返回值
sum_result = sum_2_num(1.2, 3)

print("计算结果是：%.2f" % sum_result)
