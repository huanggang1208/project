class Game(object):
    # 类属性：历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法（方法内部不需要访问实例属性和类属性）：显示帮助信息
    @staticmethod
    def show_help():
        print("帮助信息：让狗进入大门")

    # 类方法（方法内部只需要访问类属性）：显示历史记录得分
    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    # 实例方法（方法内内部需要访问实例属性）
    def start_game(self):
        print("%s马上开始游戏" % self.player_name)


# 查看游戏帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
xiaoming = Game("小明")
xiaoming.start_game()
