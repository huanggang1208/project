hello_str = "hello world"

# 判断是否以指定字符串开始
print(hello_str.startswith("h"))

# 判断是否以制定字符串结束
print(hello_str.endswith("d"))

# 查找指定字符串
# index也可以查找指定字符串
# index如果字符串中没有指定字符，会报错
# find如果字符串中中没有指定字符，则会返回-1
print(hello_str.find("llo"))
print(hello_str.find("x"))

# 替换字符串
# 注意，replace不会修改原有字符串
print(hello_str.replace("world", "python"))
print(hello_str)