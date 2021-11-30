# 记录所有的名片字典

cards_list = []


def show_menu():
    """显示功能菜单表"""
    print("#" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新增名片")
    print("2.查看全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("#" * 50)


def new_card():
    """新增名片"""
    print("*" * 50)
    print("【新增名片】")

    # 提示用户添加信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 用户输入的信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 将名片字典保存在列表中
    cards_list.append(card_dict)

    print(cards_list)

    # 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def all_cards():
    """查看全部名片"""
    print("*" * 50)
    print("【查看全部名片】")

    # 判断是否存在名片，不存在就提示用户
    if len(cards_list) == 0:
        print("当前没有名片纪录，请使用新增功能！")

        # return可以返回执行结果
        # return下方的代码不会被执行
        # 如果return后面没有任何内容，表示会返回到调用函数的位置
        # 不会返回任何的结果
        return

    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t\t\t")

    print("")
    # 打印分割线
    print("-" * 50)

    # 单行遍历名片列表依次输出名片信息
    for card_dict in cards_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" %
              (card_dict["name"],
               card_dict["phone"],
               card_dict["qq"],
               card_dict["email"]))


def find_card():
    """查询名片"""
    print("*" * 50)
    print("【查询名片】")

    # 提示用户需要查找的姓名
    find_name = input("请输入需要查询的名字：")

    # 遍历名片列表，如果没有找到名片，就需要提示用户
    for card_dict in cards_list:
        if card_dict["name"] == find_name:
            print("=" * 50)
            print("姓名\t\t\t\t电话\t\t\t\tqq\t\t\t\t邮箱")
            print("-" * 50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" %
                  (card_dict["name"],
                   card_dict["phone"],
                   card_dict["qq"],
                   card_dict["email"]))
            print("=" * 50)

            # 针对找到的名字进行修改和删除操作
            deal_card(card_dict)
            break

    else:
        print("没有找到相关名字！")


def deal_card(find_dict):
    """处理查找名片

    :param find_dict: 查找到的名片
    """
    print(find_dict)

    action_str = input("请输入想要进行的操作（1.修改 2.删除 0.返回上层）：")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名： ")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话： ")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq: ")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱： ")
        print("【修改名片】")

    elif action_str == "2":

        cards_list.remove(find_dict)
        print("【删除名片】")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message:输入的提示文字
    :return: 如果用户输入了文字就返回文字，没有输入就返回原值
    """
    # 提示用户输入内容
    result_str = input(tip_message)

    # 针对用户输入进行判断，输入结果，就直接返回输入结果
    if len(result_str) > 0:
        return result_str

    # 如果没有输入，就返回字典中原有的值
    else:
        return dict_value
