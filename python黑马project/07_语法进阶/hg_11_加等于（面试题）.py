def demo(num, num_list):

    print("函数开始！")

    num += num
    # 列表的家等于不会做相加再赋值的操作
    # 本质上是在做列表的 expend 方法
    num_list += num_list

    print(num, num_list)

    print("函数结束！")


gl_num = 9
gl_list = [1, 2, 3, 4]

demo(gl_num, gl_list)

print(gl_num, gl_list)