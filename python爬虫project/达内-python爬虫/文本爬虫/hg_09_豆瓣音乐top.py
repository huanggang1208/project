# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_09_豆瓣音乐top.py
import re
import time
import random
import csv
from urllib import request


class DoubanSpider:
    def __init__(self):
        self.url = "https://music.douban.com/top250?start={}"
        self.headers = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
        self.f = open("豆瓣音乐.csv", "a", encoding="utf-8", newline="")
        self.writer = csv.writer(self.f)
        self.all_list = []

    def get_html(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        # 调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        pattern = re.compile(r' <a class="nbg".*?alt="(.*?) - (.*?)" style="width'
                             r': 80px; max-height: 120px;" />.*? </span></div>', re.S)
        r_list = pattern.findall(html)
        print(r_list)

        # 调用数据保存函数
        self.save_html(r_list)

    def save_html(self, r_list):
        item = {}
        for r in r_list:
            film_t = (
                r[0].strip(),
                r[1].strip()
            )
            self.all_list.append(film_t)
            print(film_t)

    def run(self):
        for start in range(0, 250, 25):
            url = self.url.format(start)
            self.get_html(url)

            time.sleep(random.uniform(0, 1))

        self.writer.writerows(self.all_list)
        self.f.close()


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
