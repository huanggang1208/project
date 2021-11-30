# 定义python_score，c_score两门成绩
python_score = int(input("输入python成绩："))
c_score = int(input("输入c语言成绩："))

# 只要两门中有一门超过60分就算合格\
if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("考试不合格")
