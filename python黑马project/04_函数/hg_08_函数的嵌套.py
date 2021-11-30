def test1():
    print("*" * 5)


def test2():
    print("-" * 5)

    # 函数的嵌套调用
    test1()

    print("-" * 5)


test2()
