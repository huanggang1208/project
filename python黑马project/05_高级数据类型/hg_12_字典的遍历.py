name_dict = {"name": "xiaoming",
             "age": "18",
             "height": "1.85"}
# k 是在循环体中获取到字典中的key
for k in name_dict:
    print("%s-%s" % (k, name_dict[k]))
