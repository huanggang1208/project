def print_line3(char, times):
    """可以输入任意符号任意个数组成分割线"""
    print(char * times)


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


name = "努力学习Python"
