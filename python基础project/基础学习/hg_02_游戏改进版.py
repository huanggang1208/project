import random
print("**********欢迎来到改进版游戏体验*********")


answer = random.randint(1, 10)
temp = input("请你猜猜这个10以内随机数是多少：")
think = int(temp)
times = 1

# 循环语句，猜的和结果不一样 和 次数小于三次循环循环体
while (think != answer) and (times < 3):
    if think < answer:
        print("小了，兄弟")
    else:
        print("大了，兄弟")

    temp = input("要不再试试吧，你猜几：")
    think = int(temp)
    times += 1

if (think == answer) and (times <= 3):
    print("你猜对啦！")

else:
    print("给你三次机会都猜错了，不玩了")


