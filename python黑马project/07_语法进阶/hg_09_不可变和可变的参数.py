def demo(num, num_list):
    print("实验开始了！")
    # 在函数内部，针对参数使用的赋值语句，不会修改函数外部的实参变量
    num = 100
    num_list = [1, 2, 3]

    print(num, num_list)
    print("函数执行完成！")


gl_num = 50
gl_list = [3, 2, 1]
demo(gl_num, gl_list)
print(gl_num, gl_list)