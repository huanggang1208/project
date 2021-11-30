class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地面积%.2f" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
sofe = HouseItem("沙发", 3.5)
chair = HouseItem("桌子", 2.36)

print(bed)
print(sofe)
print(chair)
