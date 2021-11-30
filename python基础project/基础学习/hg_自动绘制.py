# 调用数据文档自动绘制
import turtle as t
t.setup(800, 600, 0, 0)
t.title("自动绘制图形")
t.pensize(5)
t.pencolor("red")
# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", " ")
    datals.append(list(map(eval, line.split(","))))
f.close()
# 自动绘制 数据接口定义0：前进，1：1右转0左转，2：转角度，345：RGB色值
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
