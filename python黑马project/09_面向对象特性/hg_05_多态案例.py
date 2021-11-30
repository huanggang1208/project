class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s开开心心玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s飞到天上玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s快乐玩耍" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 创建一个狗对象
wangcai = Dog("旺财")
# 创建一个人对象
xiaoming = Person("小明")
# 调用人和狗玩
xiaoming.game_with_dog(wangcai)
