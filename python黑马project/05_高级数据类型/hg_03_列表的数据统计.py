name_list = ["孙悟空", "猪八戒", "沙悟净", "孙悟空"]

# len 可以技计数列表的长度
len_list = len(name_list)

print("列表中有 %d 个元素" % len_list)

# count 方法可以计数列表中某一个元素出现的次数
count_list = name_list.count("孙悟空")

print("孙悟空在列表里出现了 %d 次" % count_list)
