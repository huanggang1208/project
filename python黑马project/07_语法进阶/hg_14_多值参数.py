# 参数前加一个*可以接受一个元组，加两个*可以接收一个字典
def demo(num, *nums, **num_list):
    print(num)
    print(nums)
    print(num_list)


demo(1)
demo(1, 3, 5, 5, name='小明', age="18")
