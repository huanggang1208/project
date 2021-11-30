# 要求：
# 1.将空白字符全部去掉
# 2.使用”“作为分隔符，拼接成一个整齐的字符串
poem_str = "静夜思\t  李白\t 床前明月光\t\n  疑是地上霜\t\n  举头望明月\t 低头思故乡\n"
print(poem_str)

# 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 拼接字符串
result = " ".join(poem_list)
print(result)