class Cat:
    def drink(self):
        print("小猫爱喝水！")

    def eat(self):
        print("小猫爱吃鱼！")


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
