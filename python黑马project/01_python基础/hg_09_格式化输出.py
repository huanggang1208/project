# 定义name，输出格式化
name = "hlo"
print("我的名字叫 %s ，请多多关照" % name)

# 定义整数变量student_no ,输出我的学号是000001
student_no = 5
print("我的学号是%06d" % student_no)

# 定义小数，苹果的单价5.00，重量6.00，价格30.00
price = 6
weight = 6
money = price * weight
print("单价 %.2f 元/斤，重量 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))

# 定义一个小数scale，输出数据是25.02%
scale = 25
print("数据比例: %.2f%%" % scale)
