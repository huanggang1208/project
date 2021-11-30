info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1.取值和取索引
print(info_tuple[0])
# index 可以知道元素在元组中的索引
print(info_tuple.index("zhangsan"))

# 统计计数
print(info_tuple.count("zhangsan"))

# 元组中元素的个数
print(len(info_tuple))