class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s是我" % self.name)

    def __del__(self):
        print("%s去了" % self.name)

    def __str__(self):

        # 必须返回一个字符串
        return "我是一只小猫,名字是%s" % self.name


# tom是一个全局变量
tom = Cat("tom")
print(tom)
