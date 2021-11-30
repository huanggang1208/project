def print_line():
    print("*" * 50)


print_line()


def print_line2(char):
    """可以输入任意符号组成的分割线"""
    print(char * 50)


print_line2("-")


def print_line3(char, times):
    """可以输入任意符号任意个数组成分割线"""
    print(char * times)


print_line3("$", 10)


def print_lines(char, times):
    """完成多行分隔线，可以输入任意符号和个数
    :param char: 任意符号
    :param times: 任意个数
    """
    # 使用while循环
    row = 0

    while row < 5:

        print_line3(char, times)

        row += 1


print_lines("5", 5)

