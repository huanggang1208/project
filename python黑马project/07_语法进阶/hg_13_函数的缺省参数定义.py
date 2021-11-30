def print_info(name, gender=True):
    """
    :param name: 班级上同学的姓名
    :param gender:True是男生 False是女生
    """
    gender_txt = "男生"

    if not gender:
        gender_txt = "女生"

    print("%s是%s" % (name, gender_txt))


print_info("小米", False)
print_info("小明")
print_info("小美", False)
