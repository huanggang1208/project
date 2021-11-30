# 类名字首字母要大写
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是{1}.".format(self.name, self.score))


s1 = Student("herry", "89")
s1.say_score()
