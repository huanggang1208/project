class Women:
    def __init__(self, name):
        self.name = name
        # 私有属性在参数前加__
        self.__age = 19

    def secret(self):
        # 在对象方法内部可以访问私有属性
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")
# 在外界不能直接访问私有属性
print(xiaofang.__age)
xiaofang.secret()
print(xiaofang)
# 在外界不能直接访问私有方法，私有方法在方法前加__
xiaofang.__secret()
