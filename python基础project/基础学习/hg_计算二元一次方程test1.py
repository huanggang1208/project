import math

def eryuan(a, b, c, ):
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("无根")
        elif delta == 0:
            s = -b / (2 * a)
            print("唯一根x=", s)
        else:
            root = math.sqrt(delta)
            x1 = (-b + root) / (2 * a)
            x2 = (-b - root) / (2 * a)
            print("x1=", x1, "\t", "x2=", x2)

eryuan(2,4,2)



