# 学习分支与循环
temp = input("请输入你的成绩：")
score = float(temp)
true_score = (0 <= score <= 100)

while true_score:

    if 85 <= score <= 100:
        print("A")

    elif 75 <= score < 85:
        print("B")

    elif 60 <= score < 75:
        print("C")

    elif 0 <= score < 60:
        print("D")

    break

if not true_score:
    print("请输入0~100的分数!")
    temp = input("请再输入你的成绩：")
    score = float(temp)

    if 85 <= score <= 100:
        print("A")

    elif 75 <= score < 85:
        print("B")

    elif 60 <= score < 75:
        print("C")

    elif 0 <= score < 60:
        print("D")


