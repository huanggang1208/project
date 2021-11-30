# 1.定义一个整数变量年龄
age = int(input("输入年龄："))

# 2.年龄在0-120之间
if 0 <= age <= 100:
    print("年龄正确")
else:
    print("年龄错误")