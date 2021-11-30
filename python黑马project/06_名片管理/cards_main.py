# ！/usr/bin/python3


import cards_tools

# 无限循环，由用户自主选择什么时候退出循环
while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择想进行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1/2/3、是针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 查看全部
        elif action_str == "2":
            cards_tools.all_cards()
        # 查询名片
        elif action_str == "3":
            cards_tools.find_card()

        # 如果不想当时协相关代码，可以用pass当做占位符
        # 就不会执行相关条件语句
        pass

    # 0 是退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")

        break

    # 其他是无法进行的操作，需要提醒
    else:
        print("输入错误，请重新选择")
