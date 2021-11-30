def measure():
    """测量温度和湿度"""
    print("测量开始...")
    temp = "测量温度为45°"
    wetness = "测量湿度为20°"
    print("测量结束...")

    # 元组可以包含多个数据，因此可以使用元组来返回一个函数中多个变量的值
    # 如果返回的数据是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness


# 元组
result = measure()
print(result)

# 如果需要单独处理温度和湿度
# 使用下面的方式进行处理不方便
print(result[0])
print(result[1])

# 我们可以定义全局变量的方式进行调用
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)