# 利用蒙特卡罗方法随机撒点计算圆周率
import time
import random

darts = 1000 * 1000 * 20  # 总共撒点数
hits = 0.0  # 中点的个数
start = time.perf_counter()  # 开始撒点的时间
for i in range(1, darts + 1):  # 遍历所有撒点数
    x, y = random.random(), random.random()  # 随机中点在x坐标和y坐标的位置
    # 判断随机中点是否在圆内
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / darts)
print("π的值是：{0}, 运行时间是：{1:.6f}".format(pi, time.perf_counter() - start))
