class People:

    def __init__(self, name, weight):

        # self.属性名 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫%s，体重是%.2fkg" % (self.name, self.weight)

    def run(self):

        print("%s跑步的话，体重会减少哦" % self.name)
        self.weight -= 0.5

    def eat(self):

        print("%s吃东西会变得更胖" % self.name)
        self.weight += 1


xiaoming = People("小明", 75)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

# 小美爱跑步
xiaomei = People("小美", 45)

xiaomei.eat()
xiaomei.run()

print(xiaomei)
