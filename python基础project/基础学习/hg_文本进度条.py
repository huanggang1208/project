# 文本进度条
import time
scale = 10
print("------执行开始------")
for i in range(11):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale)*100
    print("{:<3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("------执行结束------")

# 文本进度条 单行刷新
import time
for x in range(101):
    print("\r{:3}%".format(x), end="")
    time.sleep(0.1)



