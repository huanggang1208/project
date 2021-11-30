# 连续输出5行小星星，每排递增
# 定义一个行的变量 row
row = 1

while row <= 5:

    # 定义一个列的变量 col
    col = 1

    # 开始嵌套循环
    while row >= col:

        print("*", end="")

        col += 1

    print("")

    row += 1