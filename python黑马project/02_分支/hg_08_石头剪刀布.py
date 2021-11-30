# 导入工具包
import random

# 1.控制台输入要出的拳（石头1，剪刀2，布3）
player = int(input("您需要出的拳（石头1，剪刀2，布3）："))

# 2.电脑需要随机出拳
computer = random.randint(1,3)

print("玩家出的拳是 %d - 电脑出的拳是 %d" % (player, computer))

# 3.比较胜负
"""
玩家胜利：
石头 胜 剪刀
剪刀 胜 布
布 胜 石头
"""
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利")
# 玩家和电脑出的一样，平局
elif player == computer:
    print("平局")

# 其他情况，电脑胜利
else:
    print("电脑获胜")


