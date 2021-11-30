class A:
    def test(self):
        print("方法1")

class B:
    def demo(self):
        print("demo")

class C(A, B):
    """多继承可以让子对象同时具有多个
    父类的属性和方法"""

    """如果不同的父类中存在同名的方法，应该尽量避免使用多继承"""
    pass

c = C()
c.demo()
c.test()