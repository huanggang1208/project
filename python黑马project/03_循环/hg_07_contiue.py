# 定义一个变量 i
i = 0

# 开始循环体
while i < 10:

    if i == 3:
        # 如果要使用 continue 这个函数，在使用之前要
        i += 1

        continue

    print(i)

    i += 1

print("循环结束！")
