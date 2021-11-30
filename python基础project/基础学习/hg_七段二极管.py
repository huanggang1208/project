# 获取系统年月日，绘制二极管时间格式
import turtle, time


def drawGap():
    turtle.penup()
    turtle.fd(5)


def drawline(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(digit):
    drawline(True) if digit in [2, 3, 5, 6, 8, 4, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 5, 6, 7, 8, 4, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(30)


def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == "-":
            turtle.write("年",font=[50])
            turtle.pencolor("green")
            turtle.penup()
            turtle.fd(50)
        elif i == "+":
            turtle.write("月",font=[50])
            turtle.pencolor("blue")
            turtle.penup()
            turtle.fd(50)
        elif i == "=":
            turtle.write("日",font=[50])
            turtle.penup()
            turtle.fd(50)
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 400, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m+%d=",time.gmtime()))  # 需要是字符串而不是数值
    turtle.hideturtle()
    turtle.done

main()

