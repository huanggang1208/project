# changetemp.py
tempstr = input("请输入带格式的温度：")
if tempstr[-1] in ["f", "F"]:
    C = (eval(tempstr[0: -1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
elif tempstr[-1] in ["c", "C"]:
    F = 1.8 * eval(tempstr[0: -1]) + 32
    print("转换后的温度显示是{:.2f}F".format(F))
else:
    print("输入格式一定是错误的！")
