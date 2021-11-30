class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 枪的子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("【%s】没有子弹了" % self.model)

            return
        # 发射子弹， -1
        self.bullet_count -= 1

        # 提示发射信息
        print("[%s]砰砰砰。。。[%d]" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):
        # 定义一个姓名
        self.name = name
        # 枪
        self.gun = None

    def fire(self):
        # 判断士兵是否有枪
        if self.gun is None:
            print("[%s]还没有枪。。" % self.name)

            return
        # 高喊口号
        print("冲啊。。[%s]" % self.name)

        # 让枪填子弹
        self.gun.add_bullet(50)

        # 让枪发子弹
        self.gun.shoot()


# 1创建枪对象
ak47 = Gun("ak47")

# 2创建士兵对象
Xusanduo = Soldier("许三多")
Xusanduo.gun = ak47
Xusanduo.fire()

print(Xusanduo.gun)
