# 定义一个类
class Cat:
    def drink(self):
        # 哪一个对象调用的方法，self就是那个对象的引用
        print("%s爱喝水！"% self.name)

    def eat(self):
        print("%s爱吃鱼！"% self.name)


# 创建猫对象
tom = Cat()
tom.name = "汤姆"

tom.eat()
tom.drink()

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "小懒猫"

lazy_cat.eat()
lazy_cat.drink()
