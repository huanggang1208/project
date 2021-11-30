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


# 创建枪对象
ak47 = Gun("ak47")

ak47.add_bullet(50)
ak47.shoot()
