# 计算0-100累加求和

# 定义一个最终输出的结果
result = 0

# 定义一个变量
i = 0

# 开始循环体
while i <= 100:
    print(i)

    # 让每次最终结果都和 i 相加
    result += i

    # 处理计数器
    i += 1

# 输出最终结果
print("0-100求和： %d " % result)
