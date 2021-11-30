class Animal:
    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def run(self):
        print("run")

    def drink(self):
        print("drink")


class Dog(Animal):
    def shark(self):
        print("shark")

class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")
    # 如果子类中重写了父类的方法，会调用子类中的方法
    # 不会使用父类中的方法
    def shark(self):
        # 针对子类特有的需求，编写代码
        print("aoaoaoao")
        # 使用super（）.调用原本在父类中的方法
        super().shark()
        # 增加其他子类代码
        print("a;sldjfas;djfa;lsdkj")

dog = XiaoTianQuan()
dog.drink()
dog.eat()
dog.run()
dog.sleep()
dog.shark()
