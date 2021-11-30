name_dict = {"name": "xiaoming",
                 "age": 18,
                 "gender": True,
                 "height": 1.85}

# 键值对数量计数
dict_len = len(name_dict)
print(dict_len)

# 合并字典
temp_dict = {"wojiao": "xiaohuang",
             "aihao": "daqiu"}
name_dict.update(temp_dict)

# 清空字典
name_dict.clear()

print(name_dict)


