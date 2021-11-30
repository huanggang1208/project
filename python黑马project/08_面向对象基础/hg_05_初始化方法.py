class Cat:

    #
    def __init__(self):
        print("这个是初始化方法")

        # self.属性名就是该属性的初始值
        self.name = "tom"

# 用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat()
print(tom.name)

