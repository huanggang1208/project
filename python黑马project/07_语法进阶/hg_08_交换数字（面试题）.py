a = 6
b = 100

# 解法1:使用其他变量
# c = a
# a = b
# b = c
# print(a, b)

# 解法2：不使用其他变量
# a = a + b  # a(106) = a(6) + b(100)
# b = a - b  # b(6) = a(106) - b(100)
# a = a - b  # a(100) = a(106) - b(6)
# print(a, b)

# 解法3：Python专用
# 提示：等号后面是一个元组，可以省略括号
# a, b = (b, a)
a, b = b, a
print(a, b)