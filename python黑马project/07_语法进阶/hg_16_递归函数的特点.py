def sum_numbers(num):

    print(num)
    # 递归的出口，当满足某个条件时，不在执行函数
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    # 自己调用自己
    sum_numbers(num - 1)


sum_numbers(4)