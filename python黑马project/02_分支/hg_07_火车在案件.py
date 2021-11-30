# 1.定义一个布尔型变量，has_ticket表示是否有票
has_ticket = True

# 2.定义一个变量knife_length表示携带刀具长度
knife_length = float(input("检查刀具长度cm:"))

# 3.检查是否有车票，有车票就进入安检，没有车票就不让进
if has_ticket:
    print("车票检查通过，马上进入安检")

    # 安检时，检查刀具的长度如果长度大于20，则输出安检不通过
    if knife_length > 20:
        print("您携带的刀具太长了，有 %d cm长" % knife_length)
        print("安检不通过")

    # 如果刀具长度没有20，则输出安检通过
    else:
        print("安检通过！")

# 没有车票就输出先买票
else:
    print("没有车票，请先买票！")


