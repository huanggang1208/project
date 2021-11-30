name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
# 取值
print(name_list[0])

# 取索引
print(name_list.index("lisi"))

# 2.修改
name_list[2] = "王五"

# 3.增加
# append方法 可以在列表末尾增加
name_list.append("小东西")
# insert方法 可以在两者之间增加
name_list.insert(1, "王老五")
# extend方法 可以追加另外一个列表到一个列表中
hg_list = ["孙悟空", "猪八戒", "沙悟净"]
name_list.extend(hg_list)

# 4.删除
# remove方法可以删除指定
name_list.remove("猪八戒")
# pop方法默认删除最后一个
name_list.pop()
# pop方法可以删除其中一个
name_list.pop(1)
# clear方法可以删除所有
name_list.clear()


print(name_list)