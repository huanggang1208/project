# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_24_多线程示例.py
from threading import Thread


def spider():
    print("我是多线程！")


t_list = []
for i in range(5):
    t = Thread(target=spider)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()
