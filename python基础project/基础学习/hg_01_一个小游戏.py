import random
i = 0
while i < 3:

    temp = input("请输入你想选择的数字：")
    guess = int(temp)
    answer = random.randint(1, 10)

    if guess == answer:
        print("你可真厉害！")
        break

    elif guess < answer:
        print("你猜小了！")

    else:
        print("你猜大了啦！")

    i = i + 1

print("游戏结束啦！不玩了！")