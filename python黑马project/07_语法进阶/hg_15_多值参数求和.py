def sum_numbers(*args):

    num = 0

    print(args)
    # 求和使用循环遍历
    for n in args:
        num += n

    return num


result = sum_numbers(1, 4, 5)
print(result)