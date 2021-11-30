students = [
    {"name": "xiaoming"},
    {"name": "xiaohua"}
]

# 在循环体中查找指定的姓名
find_name = "xiaming"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)

        # 如果已经找到，就不在执行后续的代码
        break

else:
    print("没有找到 %s" % find_name)

print("循环结束")