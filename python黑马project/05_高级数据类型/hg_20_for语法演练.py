for num in [2, 3, 4, 5, 6]:

    print(num)

    if num == 4:

        break

else:
    # 如果循环体内部用break退出了循环
    # 那么else下方的代码就不会执行
    print("可以吗？")

print("循环结束！")