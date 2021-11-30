def demo(*args, **kwargs):

    print(args)
    print(kwargs)


tuple = (1, 2, 3)
dict = {"name": "hg", "dianhua": "234234"}
# 如果不作特殊说明，会将两个实参定义到第一个形参
# demo(tuple, dict)
demo(*tuple, **dict)