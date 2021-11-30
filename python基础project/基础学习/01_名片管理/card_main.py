# ！ C:\Users\aspire\AppData\Local\Microsoft\WindowsApps\python3.exe

import card_tools

# 利用无限循环看在什么时候退出循环
while True:
    # 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择要执行的操作：")
    print("你操作的选项是【%s】" % action_str)

    # 123是对名片操作
    if action_str in ["1", "2", "3"]:
        # 1是新增名片
        if action_str == "1":
            # 新增名片
            card_tools.new_card()

        # 2是显示全部名片
        elif action_str == "2":
            card_tools.show_all()

        # 3是查询名片
        elif action_str == "3":
            card_tools.search_card()

    # 0是退出操作
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他数字操作错误
    else:
        print("输入错误！重选操作：")
