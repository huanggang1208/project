# 输入苹果的单价
price_str = input("苹果的单价：")

# 输入苹果的重量
weight_str = input("苹果的重量:")

# 计算苹果的价格
# 字符串之间不能做乘法运算
# 首先要将苹果的单价和重量转换成浮点数数据类型
price = float(price_str)

weight = float(weight_str)

# 现在计算苹果的价格
money = price * weight

print(money)
