# 记录所有的字典
card_list = []


def show_menu():
    # 显示菜单
    print("*" * 50)
    print("欢迎使用名片系统")
    print("1-新增名片")
    print("2-显示全部名片")
    print("3-查询名片")
    print("0-退出系统")
    print("*" * 50)


def new_card():
    # 新增名片
    print("-" * 50)
    print("新增名片")
    # 1提示用户输入用户的详细信息
    name_str = input("请输入名字：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 3将名片字典添加到列表中
    card_list.append(card_dict)

    # 4提示用户添加成功
    print("添加%s的名片成功" % name_str)


def show_all():
    # 查看全部名片
    print("-" * 50)
    print("查看全部名片")
    print("=" * 50)
    if len(card_list) == 0:
        print("没有数据名片,请添加")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历列表里的字典
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    # 查询名片
    print("-" * 50)
    print("查询名片")
    print("=" * 50)
    # 提示搜索名字
    find_name = input("请输入要搜索的名字：")
    # 遍历名字，搜索名字，没找到提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("*" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 对找到的名片进行修改、删除操作，引用函数操作
            deal_card(card_dict)

            break
    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """
处理找到的名片
    :param find_dict: 找到的名片
    """
    print(find_dict)

    action_str = input("请输入要执行的操作：（1 修改，2 删除， 0 返回上级菜单）")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"])
        find_dict["phone"] = input_card_info(find_dict["phone"])
        find_dict["qq"] = input_card_info(find_dict["qq"])
        find_dict["email"] = input_card_info(find_dict["email"])

        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片")


def input_card_info(dict_value, tip_message):
    """
输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入提示文字
    :return: 有值返回，没有值就返回字典中原有值
    """
    # 提示用户输入内容
    result_str = input(tip_message)

    # 针对用户输入进行判断，如果由内容直接返回
    if len(result_str) > 0:

        return result_str

    # 如果没有输入内容，返回字典中原有的值
    else:
        return dict_value
