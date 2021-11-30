# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_07_猫眼电影top100csv.py
# 抓取猫眼电影top100电影列表
from urllib import request
import re
import time
import random
import csv


class MaoyanSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        # 添加计数变量
        self.i = 0
        self.f = open("猫眼top100.csv", "a", newline="")
        self.writer = csv.writer(self.f)
        # 定义一个空列表，存所有电影信息的大列表
        self.all_film_list = []

    def get_html(self, url):
        """获取响应内容"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析函数"""
        pattern = re.compile('<p class=.*?title="(.*?)" class=.*?<p class="star">(.*?)</p>'
                             '.*?<p class="releasetime">(.*?)</p>', re.S)
        # r_list = [('张国荣','霸王别姬','1993'),(),()]
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for r in r_list:
            film_t = (
                r[0].strip(),
                r[1].strip(),
                r[2].strip()
            )
            # 每个电影处理之后添加到总列表中了
            self.all_film_list.append(film_t)
            print(film_t)
            self.i += 1

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url)
            # 控制爬虫频率
            time.sleep(random.randint(1, 2))
        # 所有页面抓完之后开始写入
        self.writer.writerows(self.all_film_list)
        self.f.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
    print("电影数量", spider.i)
