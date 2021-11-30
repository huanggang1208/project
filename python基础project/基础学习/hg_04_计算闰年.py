# 用for循环计算闰年

# 使用break结束循环
for year in range(2020, 2050):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break

print("2020年之后的第一个闰年是%d年" % year)


# 使用continue继续循环
for year in range(2020, 2050):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        continue

print("2020年到2050年之间的最后一个闰年是%d年" % year)