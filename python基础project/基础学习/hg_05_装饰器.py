def log(hg):
    def wrapper():
        print("开始调用eat()函数")
        hg()
        print("结束调用eat()函数")

    return wrapper


@log
def eat():
    print("开始吃了")


eat()


def funX(x):
    def funY(y):
        return x * y

    return funY


temp = funX(8)
temp(5)

