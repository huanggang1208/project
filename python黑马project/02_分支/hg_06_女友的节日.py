# 1.定义一个节日变量holiday_name
holiday_name = str(input("请输入节日名称："))

# 2.如果是情人节，就送玫瑰和大餐
if holiday_name == "情人节":
    print("送玫瑰")
    print("吃大餐")
# 3.如果是圣诞节，就送苹果
elif holiday_name == "圣诞节":
    print("松苹果")
# 4.如果是生日，那就送生日蛋糕
elif holiday_name == "生日":
    print("松生日蛋糕")
# 5.都不是那就吃大餐
else:
    print("那就吃大餐吧")