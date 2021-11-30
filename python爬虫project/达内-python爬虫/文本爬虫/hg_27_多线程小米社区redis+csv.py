# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_26_多线程小米社区.py

# 多线程适用增量爬虫会出现一些问题
import csv
# import json
import requests
import time
import random
from fake_useragent import UserAgent
# import os.path
from queue import Queue
from threading import Thread, Lock
import sys
import redis
from hashlib import md5


class Xiaomi:
    def __init__(self):
        self.url = "https://prod.api.xiaomi.cn/community/square?start={}&limit=10"
        self.i = 0
        # 创建队列，存储多个待抓取的url地址（全局变量）
        self.q = Queue()
        # 创建一把锁
        self.lock = Lock()
        self.r = redis.Redis(host="localhost", port=6379, db=0)
        """字典保存到csv格式文件内"""
        # 列名
        self.headers = ["id", "userid", "type", "title", "picUrl"]
        self.f = open("小米社区info.csv", "a", encoding="utf-8", newline="")
        self.writer = csv.DictWriter(self.f, fieldnames=self.headers)
        # 预览列名
        self.writer.writeheader()

    def url_in(self):
        """将url入队列"""
        for page in range(1, 40):
            url = self.url.format(page)
            # 入队列,Queue.put()方法
            self.q.put(url)

    def parse_html(self):
        """线程事件函数：获取url，请求，解析，处理数据"""
        while True:
            # 判断队列是否为空，如果空队列使用get()会造成队列堵塞
            # 上锁
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                # 释放锁
                self.lock.release()
                headers = {"user-agent": UserAgent().random}
                html = requests.get(url=url, headers=headers).json()
                time.sleep(random.randint(0, 1))
                item = {}
                # 在json源代码中都是以字典形式存在的record是字典
                records = html["entity"]["records"]
                # print(records)
                for record in records:
                    finger = self.md5_func(record)
                    if self.r.sadd("Xiaomi:fingers", finger) == 1:
                        if "pic" in record:
                            item["id"] = record["id"]
                            item["userid"] = record["userId"]
                            item["type"] = record["type"]
                            item["title"] = record["title"]
                            item["picUrl"] = record["pic"]
                            self.writer.writerow(item)
                            self.i += 1
                            print(item)
                    else:
                        sys.exit("已经抓取完了！")
            else:
                # 如果队列为空，就结束任务
                # 队列上锁后，队列为空也需要释放锁
                self.lock.release()
                break

    def md5_func(self, record):
        s = md5()
        s.update(str(record).encode("utf-8"))
        return s.hexdigest()

    def run(self):
        # 先让url入队列
        self.url_in()
        # 创建多线程运行
        t_list = []
        for i in range(3):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()
        print("抓取%d条信息" % self.i)
        self.f.close()


if __name__ == '__main__':
    start_time = time.time()
    spider = Xiaomi()
    spider.run()
    end_time = time.time()
    print(end_time - start_time)
