class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s是我" % self.name)

    def __del__(self):
        print("%s去了" % self.name)


# tom是一个全局变量
tom = Cat("tom")
print(tom.name)
print("*" * 5)
