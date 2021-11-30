
# 定义一个函数sum_numbers
# 能够接收一个num的整数参数
# 计算1+2+3.。。+num的值

def sum_numbers(num):
    # 出口
    if num == 1:
        return 1

    # 数字的累加num+（1...num-1）
    # 假设sum_numbers可以正确处理（1...num-1）
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(100)
print(result)
