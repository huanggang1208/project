class Tool(object):
    # 使用赋值语句增加一个类属性
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("小刀")
tool2 = Tool("锤子")
tool3 = Tool("斧头")

# 输出工具对象总数
print(Tool.count)
print(tool3, tool2, tool1)