name_dict = {"name": "xiaoming"}

# 取值
name = name_dict["name"]
print(name)
# 取值中若key不存在，会报错

# 增加、修改
# 如果key不存在，会新增键值对
name_dict["age"] = 18
# 如果key存在，会新增修改键值对
name_dict["name"] = "小华"

# 删除
name_dict.pop("name")
# 如果需要删除的key不存在，那么程序会报错

print(name_dict)